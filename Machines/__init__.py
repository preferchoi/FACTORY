import asyncio
import random
import Materials


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
