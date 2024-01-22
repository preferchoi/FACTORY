import Machines


class Factories:
    """
    공장을 나타내는 클래스입니다.
    각 공장은 여러 개의 기계(Machines) 인스턴스를 관리합니다.
    이 클래스는 기계를 공장에 추가하고, 공장의 전체 기계 목록을 관리하는 기능을 제공합니다.
    속성:
        machines (list of Machines): 이 공장에서 관리하는 기계들의 리스트입니다.
    """
    fac_id_counter = 0
    def __init__(self, machines: [Machines] = []):
        """
        Factories 클래스의 인스턴스를 초기화합니다.
        매개변수:
            machines (list of Machines): 이 공장에서 초기에 관리할 기계들의 리스트입니다. 기본값은 빈 리스트입니다.
        """
        Factories.fac_id_counter += 1
        self.id = Factories.fac_id_counter
        self.machines = machines

    def add_machine(self, machine: Machines):
        """
        새로운 기계를 공장에 추가합니다.
        이 메서드는 새로운 Machines 인스턴스를 받아 공장의 기계 목록에 추가합니다.
        매개변수:
            machine (Machines): 공장에 추가할 새로운 기계입니다.
        """
        self.machines.append(machine)
