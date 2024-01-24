from Machines import Machines


class Factories:
    id_counter = 0
    instance = {}

    def __init__(self):
        Factories.id_counter += 1
        Factories.instance[Factories.id_counter] = self
        self.id = Factories.id_counter
        self.size = 3
        self.machines = [
            Machines(input_items={"iron_ore": 1, "coal": 1, "money": 1}, output_items={"sintered_steel": 1}),
            Machines(input_items={"coal": 1, "money": 1}, output_items={"coke": 1}),
            Machines(input_items={"sintered_steel": 1, "coke": 1, "money": 1}, output_items={"steel": 1, "slag": 1}),
        ]

    def add_machine(self, machine_id: int):
        try:
            machine = Machines.instance[machine_id]
            if self.size <= len(self.machines):
                return {"status": "fail"}
            self.machines.append(machine)
            return {"status": "success"}

        except KeyError:
            return {"status": "fail"}
