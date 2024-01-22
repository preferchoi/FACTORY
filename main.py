from fastapi import FastAPI
import Managers
from Factories import Factories

app = FastAPI()

Factory = Factories()
Factory_manager = Managers.InstanceManager()
Factory_manager.add_instance(Factory)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/get_factories")
async def get_factories():
    return {"Factory": [{"id": instance.id} for instance in Factory_manager.get_instances()]}


@app.get("/get_factory")
async def get_factory():
    return {"Factory": Factory_manager.get_instances()}
