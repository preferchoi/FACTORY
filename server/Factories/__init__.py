from Machines import Machines


class Factories:
    id_counter: int = 0
    instance: object = {}

    def __init__(self):
        Factories.id_counter += 1
        Factories.instance[Factories.id_counter] = self
        self.id: int = Factories.id_counter
        self.size: int = 3
        self.machines: [Machines] = [
            Machines(input_items={"iron_ore": 1, "coal": 1, "money": 1}, output_items={"sintered_steel": 1},
                     process_time=2, error_rate=0.05),
            Machines(input_items={"coal": 1, "money": 1}, output_items={"cokes": 1}, process_time=3, error_rate=0.08),
            Machines(input_items={"sintered_steel": 1, "cokes": 1, "money": 1}, output_items={"steel": 1, "slag": 1},
                     process_time=5, error_rate=0.1),
        ]

    def add_machine(self, machine_id: int):
        try:
            machine: Machines = Machines.instance[machine_id]
            if self.size <= len(self.machines):
                return {"status": "fail"}
            self.machines.append(machine)
            return {"status": "success"}

        except KeyError:
            return {"status": "fail"}

    def size_up(self):
        if self.size > 10:
            return {"status": "fail"}
        self.size += 1
        return {"status": "success"}
