import json

from fastapi import FastAPI
from Factories import Factories
from Machines import Machines
from Materials import Materials
from fastapi.responses import StreamingResponse
import asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # 모든 메소드 허용 (GET, POST, PUT, etc.)
    allow_headers=["*"],  # 모든 헤더 허용
)

Factory = Factories()

data_update_event = asyncio.Event()

quests = {
    1: {"id": 1, "quest": {"money": 12000, "steel": 10},
        "reword": Machines(input_items={"steel": 1, "money": 10}, output_items={"steel_slab": 1},
                           process_time=8, error_rate=0.1),
        "clear": False},
    2: {"id": 2, "quest": {"money": 15000, "steel_slab": 10},
        "reword": Machines(input_items={"steel_slab": 1, "money": 10}, output_items={"hot_rolled_plate": 1},
                           process_time=10, error_rate=0.1),
        "clear": False},
    3: {"id": 3, "quest": {"money": 25000, "hot_rolled_plate": 10},
        "reword": Machines(input_items={"hot_rolled_plate": 1, "money": 20.}, output_items={"cold_rolled_plate": 1},
                           process_time=15, error_rate=0.1),
        "clear": False},
    4: {"id": 4, "quest": {"money": 38000, "cold_rolled_plate": 10},
        "reword": Machines(input_items={"steel_slab": 1, "money": 30}, output_items={"steel_billet": 1},
                           process_time=20, error_rate=0.1),
        "clear": False},
    5: {"id": 5, "quest": {"money": 45000, "steel_billet": 10},
        "reword": Machines(input_items={"steel_billet": 2, "money": 50}, output_items={"wire_rod": 1},
                           process_time=30, error_rate=0.1),
        "clear": False},
    6: {"id": 6, "quest": {"money": 60000, "wire_rod": 10},
        "reword": Machines(input_items={"steel": 5, "money": 100}, output_items={"casting": 1},
                           process_time=45, error_rate=0.1),
        "clear": False},
    7: {"id": 7, "quest": {"money": 80000, "casting": 10},
        "reword": Machines(input_items={"casting": 1, "money": 200}, output_items={"forging": 1},
                           process_time=60, error_rate=0.1),
        "clear": False},
}


@app.get("/get_factories")
async def get_factories():
    return Factory.instance


@app.get("/get_factory/{factory_id}")
async def get_factory(factory_id: int):
    try:
        return Factory.instance[factory_id]
    except KeyError:
        return {"status": "fail"}


@app.get("/add_factory")
async def add_factory():
    new_factory = Factories()
    return new_factory


@app.get("/size_up_factory/{factory_id}")
async def add_factory(factory_id: int):
    Factories.instance[factory_id].size_up()
    return Factories.instance[factory_id].size


@app.get("/get_machines")
async def get_machines():
    return Machines.instance


@app.get("/get_machine/{machine_id}")
async def get_machine(machine_id: int):
    try:
        return Machines.instance[machine_id]
    except KeyError:
        return {"status": "fail"}


@app.get("/add_machine/{factory_id}")
async def add_machine(factory_id: int):
    if Factories.instance[factory_id].size <= len(Factories.instance[factory_id].machines):
        return {"status": "fail"}
    new_machine = Machines(input_items={"steel_slab": 1, "money": 30}, output_items={"steel_billet": 1},
                           process_time=100, error_rate=0.5)
    Factories.instance[factory_id].add_machine(new_machine.id)
    return new_machine


@app.get("/run_machine/{machine_id}")
async def run_machine(machine_id: int):
    try:
        res = await Machines.instance[machine_id].run()
        data_update_event.set()
        return res
    except KeyError:
        return {"status": "fail"}


@app.get("/upgrade/{machine_id}")
async def upgrade(machine_id: int, target: str):
    try:
        res = await Machines.instance[machine_id].upgrade(target)
        return res
    except KeyError:
        return {"status": "fail"}
    return res


@app.get("/materials")
async def get_materials():
    return Materials.materials


@app.get("/materials/buy")
async def material_buy(material: str, counter: int):
    try:
        total_cost = counter * Materials.materials[material]["cost"]
        if Materials.materials["money"]["counter"] >= total_cost:
            Materials.materials["money"]["counter"] -= total_cost
            Materials.materials[material]["counter"] += counter
            data_update_event.set()
            return {"status": "success"}
        return {"status": "fail"}
    except KeyError:
        return {"status": "KeyError"}


@app.get("/materials/sell")
async def material_sell(material: str, counter: int):
    try:
        if Materials.materials[material]["counter"] >= counter:
            Materials.materials[material]["counter"] -= counter
            Materials.materials["money"]["counter"] += counter * Materials.materials[material]["cost"]
            data_update_event.set()
            return {"status": "success"}
        return {"status": "fail"}
    except KeyError:
        return {"status": "KeyError"}


@app.get("/materials_sse")
async def materials_sse():
    return StreamingResponse(send_materials(), media_type="text/event-stream")


async def send_materials():
    while True:
        await data_update_event.wait()
        data = json.dumps(Materials.materials)
        yield f"data: {data}\n\n"
        data_update_event.clear()


@app.get("/quest")
async def get_quest():
    for k, v in quests.items():
        if not v["clear"]:
            return {k: v}
    return {0: None}


@app.get("/quest_clear/{quest_id}")
async def clear_quest(quest_id: int):
    try:
        if not quests[quest_id]['clear']:
            for k, v in quests[quest_id]["quest"].items():
                if Materials.materials[k]["counter"] < v:
                    return {"status": "fail"}
            Factory.size += 1
            Factory.add_machine(quests[quest_id]["reword"].id)
            quests[quest_id]['clear'] = True
            for k, v in quests.items():
                if not v["clear"]:
                    return {"status": "success", "data": {k: v}}
            return {}
    except KeyError:
        return {"status": "KeyError"}
