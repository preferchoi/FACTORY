import asyncio
import random
from Materials import Materials


class Machines:
    id_counter: int = 0
    instance: object = {}

    def __init__(self, input_items: object, output_items: object, process_time: int = 10,
                 error_rate: float = 0.05):
        Machines.id_counter += 1
        Machines.instance[Machines.id_counter] = self
        self.id: int = Machines.id_counter
        self.input_items: object = input_items
        self.output_items: object = output_items
        self.process_time: int = process_time
        self.error_rate: float = error_rate

    async def run(self):
        try:
            for item, counter in self.input_items.items():
                if Materials.materials[item]['counter'] < counter:
                    return {"status": f"'{item}' 재료 부족"}

            for item, counter in self.input_items.items():
                Materials.materials[item]['counter'] -= counter

            res = True if random.random() > self.error_rate else False
            if res:
                for item, counter in self.output_items.items():
                    Materials.materials[item]['counter'] += counter

            await asyncio.sleep(self.process_time)

            return {"status": "success"} if res else {"status": "error"}

        except KeyError:
            return {"status": "KeyError"}

    async def upgrade(self, target):
        try:
            tmp: float = round(getattr(self, target) * random.uniform(0.7, 1.2), 2)
            if target == 'process_time' and tmp < 1:
                tmp = 1
            setattr(self, target, tmp)
            return self
        except KeyError:
            return {"status": "KeyError"}
