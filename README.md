# FACTORY

## 프로젝트 개요

제철 공장에 관한 다큐멘터리[^1]을 우연히 보게 되었다. 붉게 달아오른 쇳물과 그걸 다루는 치열한 모습에 나는 매료되었고, 해당 공정에 관한 내용을 더욱 이해해보고자 제철공정의 모습을 구현해보고자 했다.

### 사용 기술

server - Python(3.11.0), fastAPI
client - JavaScript, Vue.js(3.2.13)
design - Vuetify
util - git, chatGPT(관련 이미지 제작)

### 프로젝트 진행 경로

2024.01.20. - 프로젝트 개요 설정 및 클래스 선언
2024.01.21. - 클래스 호출 API 제작
2024.01.22. - 기계 작동 API 제작
2024.01.23. - client에 실시간 데이터 전송을 위한 SSE 생성
2024.01.24. - Vue.js로 client 생성 및 SPA로 제작
2024.01.25. - 임시 디자인 적용 및 기계 작동 로직 수정
2024.01.29.~ 30. - Vuetify 적용 및 퀘스트 추가
2024.02.02. - 이미지 제작 및 세부 디자인 변경
2024.02.05. - 퀘스트 완료 시점에 공장 데이터 갱신을 위한 vuex 적용
2024.02.08. - 프로젝트 내역 작성
2024.02.11. - Server 내역 작성

## [Server README](server/README.md)

## [Client README](web/README.md)

## 주석

[^1]:
    참고 영상 - [다큐프라임 - 원더풀 사이언스 철, 세상을 움직이다](https://www.youtube.com/watch?v=i9PEQQqzpVc&
    t=479s)
