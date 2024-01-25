import asyncio
import random
from Materials import Materials


class Machines:
    id_counter = 0
    instance = {}

    def __init__(self, input_items: object, output_items: object, process_time: int = 10,
                 error_rate: float = 0.05):
        Machines.id_counter += 1
        Machines.instance[Machines.id_counter] = self
        self.id = Machines.id_counter
        self.input_items = input_items
        self.output_items = output_items
        self.process_time = process_time
        self.error_rate = error_rate

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

            return {"status": "success"} if res else{"status": "error"}

        except KeyError:
            return {"status": "KeyError"}
