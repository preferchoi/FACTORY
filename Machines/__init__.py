import random
import time
class Machine:
    id_counter = 0

    def __init__(self, input_items: [str] = ['water'], process_time: int = 10, error_rate: float = 0.05):
        Machine.id_counter += 1
        self.id_counter = Machine.id_counter
        self.input_items = input_items
        self.process_time = process_time
        self.error_rate = error_rate

    def run(self):
        time.sleep(self.process_time)

        return "작업 완료" if random.random() < self.error_rate else 
