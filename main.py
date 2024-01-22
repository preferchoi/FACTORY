from fastapi import FastAPI
from Factories import Factories
from Machines import Machines
from Materials import Materials

app = FastAPI()

Factory = Factories()


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
        return await Machines.instance[machine_id].run()
    except KeyError:
        return {"status": "fail"}


@app.get("/materials")
async def get_materials():
    return Materials.materials
