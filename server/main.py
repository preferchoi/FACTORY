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


@app.get("/get_factories")
async def get_factories():
    return Factory.instance


@app.get("/get_factory/{factory_id}")
async def get_factory(factory_id: int):
    try:
        return Factory.instance[factory_id]
    except KeyError:
        return {"status": "fail"}


@app.get("/get_machines")
async def get_machines():
    return Machines.instance


@app.get("/get_machine/{machine_id}")
async def get_machine(machine_id: int):
    try:
        return Machines.instance[machine_id]
    except KeyError:
        return {"status": "fail"}


@app.get("/run_machine/{machine_id}")
async def run_machine(machine_id: int):
    try:
        await Machines.instance[machine_id].run()
        data_update_event.set()
        return {"status": "success"}
    except KeyError:
        return {"status": "fail"}


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
