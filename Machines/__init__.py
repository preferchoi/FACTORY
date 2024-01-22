import random
import time
import Materials


class Machines:
    """
    기계를 나타내는 클래스입니다.
    각 기계는 고유 ID, 입력 재료, 처리 시간, 오류 발생률을 갖습니다.
    기계는 주어진 입력 재료를 처리하고, 지정된 시간 동안 작업을 수행합니다.
    작업 중 오류가 발생할 수 있으며, 이는 오류 발생률에 따라 결정됩니다.

    속성:
        id_counter (int): 클래스 레벨에서 모든 기계 인스턴스에 대한 고유 ID를 추적합니다.
        id (int): 개별 기계의 고유 ID.
        input_items (dict): 기계가 처리할 입력 재료와 그 수량.
        process_time (int): 기계가 작업을 완료하는 데 필요한 시간(초).
        error_rate (float): 작업 중 오류가 발생할 확률.
    """
    id_counter = 0

    def __init__(self, input_items: object = {'water': 1}, process_time: int = 10, error_rate: float = 0.05):
        """
        기계 인스턴스를 초기화합니다.

        매개변수:
            input_items (dict): 기계가 처리할 입력 재료와 그 수량.
            process_time (int): 기계가 작업을 완료하는 데 필요한 시간(초).
            error_rate (float): 작업 중 오류가 발생할 확률.
        """
        Machines.id_counter += 1
        self.id = Machines.id_counter
        self.input_items = input_items
        self.process_time = process_time
        self.error_rate = error_rate

    def run(self):
        """
       기계를 작동시키고, 작업을 수행합니다.
       필요한 재료가 충분한지 확인하고, 충분한 경우 작업을 시작합니다.
       지정된 시간 동안 작업을 수행한 후, 오류 발생률에 따라 오류가 발생할 수 있습니다.

       반환:
           str: 작업의 결과("재료 부족", "작업 완료", "오류 발생").
       """
        # 재료 확인
        for item, required_amount in self.input_items.items():
            if item not in Materials or Materials[item] < required_amount:
                return f"'{item}' 재료 부족"

        # 재료 소모
        for item, required_amount in self.input_items.items():
            Materials[item] -= required_amount

        # 시간 소모
        time.sleep(self.process_time)

        # 오류 확률에 따른 결과 반환
        return "작업 완료" if random.random() > self.error_rate else "오류 발생"
