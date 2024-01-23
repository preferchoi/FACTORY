import json

from fastapi import FastAPI
from Factories import Factories
from Machines import Machines
from Materials import Materials
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

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


@app.get("/materials_sse")
async def materials_sse():
    return StreamingResponse(send_materials(), media_type="text/event-stream")


async def send_materials():
    while True:
        await data_update_event.wait()
        data = json.dumps(Materials.materials)
        yield f"data: {data}\n\n"
        data_update_event.clear()
