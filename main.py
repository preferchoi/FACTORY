from fastapi import FastAPI
import Managers
from Factories import Factories
from Machines import Machines

app = FastAPI()

Factory = Factories()
Factory_manager = Managers.InstanceManager()
Factory_manager.add_instance(Factory)

for _ in range(3):
    Factory.add_machine(Machines())

@app.get("/get_factories")
async def get_factories():
    """
    현재 생성된 공장의 id 값을 반환하는 api입니다.
    :return: 현재 생성된 공장의 id
    """
    return Factory_manager.get_instances()


@app.get("/get_factory/{factory_id}")
async def get_factory(factory_id: int):
    """
    특정 id 값을 가진 공장 인스턴스를 반환하는 api입니다.
    :param factory_id: 특정 공장 인스턴스의 id
    :return: 해당 id를 가진 인스턴스가 없을 경우 error 반환, 있을 경우 공장 인스턴스 반환
    """
    return Factory_manager.get_instance(factory_id)
