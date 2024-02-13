## 실행 방법

```
# factory/server 경로에서

pip install -r requirements.txt

uvicorn main:app
```

## API 명세

### /get_factories

공장 목록을 조회합니다.

### /get_factory/{factory_id}

특정 공장의 상세 정보를 조회합니다.

### /get_machines

기계 목록을 조회합니다.

### /get_machine/{machine_id}

특정 기계의 상세 정보를 조회합니다.

### /run_machine/{machine_id}

특정 기계를 작동시킵니다.

### /materials

재료 목록을 조회합니다.

### /materials/buy?material={material}&counter={counter}

재료를 구매합니다.

- material: 처리할 재료의 이름입니다.
- counter: 처리할 재료의 수량입니다.

### /materials/sell?material={material}&counter={counter}

재료를 판매합니다.

- material: 처리할 재료의 이름입니다.
- counter: 처리할 재료의 수량입니다.

### /materials_sse

서버에서 클라이언트로 실시간 업데이트를 보내기 위한 Server-Sent Events 엔드포인트입니다.

### /quest

현재 완료하지 않은 퀘스트들 중 가장 낮은 id 값을 가진 퀘스트를 조회합니다.

### /quest_clear/{quest_id}

특정 퀘스트를 완료 처리합니다.

## package 설명

### Factory

1. 전역 변수
   - id_counter: 공장의 id를 관리하는 변수
   - instance: 생성된 인스턴스의 목록, id를 key로, 인스턴스를 value로 가짐
2. 지역 변수
   - id: 생성될 시점의 id_counter, 생성 후 카운터는 +1 됨
   - size: 현재 가질 수 있는 machine의 수
   - machines: 현재 가지고 있는 machine의 목록

### Machine

1. 전역 변수
   - id_counter: 기계의 id를 관리하는 변수
   - instance: 생성된 인스턴스의 목록, id를 key로, 인스턴스를 value로 가짐
2. 지역 변수
   - id: 생성될 시점의 id_counter, 생성 후 카운터는 +1 됨
   - input_items: 작동하기 위해 필요한 물품, 물품 이름을 key로, 필요 수량을 value로 가짐
   - output_items: 작동이 완료되면 반환하는 물품, 물품 이름을 key로, 반환 수량을 value로 가짐
   - process_time: 작동하는데 소모되는 시간
   - error_rate: 오류 발생률

### Material

1. 지역 변수
   - materials: 유저가 보유하는 초기 재료. Object 형태로 재료 이름을 key로, 재료의 가격과 수를 key로 가지고 그 숫자를 value로 가진 Object 데이터를 value로 가짐
   ```
   {
        "money": {
            "cost": 1,
            "counter": 1000000
        },
    }
   ```
