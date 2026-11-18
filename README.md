<h1 align="center">Nahyeon Lim</h1>
<p align="center">Backend Developer</p>

<p align="center">
  <a href="https://develop-tracking.tistory.com/"><img src="https://img.shields.io/badge/Tech%20Blog-FF5A4A?style=for-the-badge&logo=tistory&logoColor=white" alt="Tech Blog"></a>
  <a href="https://www.linkedin.com/in/na-hyeon/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:iohyeonsz@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a>
</p>

## 소개

요청이 몰리고 작업이 중간에 실패해도, 데이터가 어긋나지 않고 다시 복구할 수 있는 서버를 만듭니다.

- 결제와 주문 시스템의 데이터 정합성과 상태 전이를 설계합니다.
- 비동기 파이프라인의 중복, 유실, 재처리 시나리오를 직접 재현해 검증합니다.
- 성능과 AI 응답 품질을 감각이 아닌 측정과 자동화된 검증으로 확인합니다.
- AI 코딩 에이전트에게 맡기는 개발은 지시문이 아니라 파일 계약과 훅으로 통제합니다.

## 기술 스택

<img src="https://skillicons.dev/icons?i=java,kotlin,go,python,spring,kafka,rabbitmq,redis&perline=8" alt="Stack">
<br>
<img src="https://skillicons.dev/icons?i=mysql,postgres,mongodb,elasticsearch,docker,kubernetes&perline=6" alt="Stack">

## 최근 실험

블로그 글과 짝을 이루는 저장소입니다. 글에 적은 숫자와 결론은 저장소의 코드로 다시 실행할 수 있습니다.

| 저장소 | 무엇을 확인했나 | 기술 |
|---|---|---|
| **[contract-first-harness](https://github.com/iohyeon/contract-first-harness)** | AI 코딩 에이전트의 실수를 지시문 대신 파일 계약과 PreToolUse 훅으로 막는 Claude Code 개발 하네스 | `Claude Code 플러그인` `Shell` |
| **[testing-in-practice](https://github.com/iohyeon/testing-in-practice)** | 구현을 일부러 틀리게 바꿨을 때 어느 테스트가 잡고 어느 테스트가 놓치는지 확인하는 연재 예제. 편마다 `part-N` 태그로 코드를 고정 | `Java 21` `Kotlin` `Spring Boot` `Mockito` |
| **[pg-insert-race](https://github.com/iohyeon/pg-insert-race)** | 두 트랜잭션이 동시에 "최댓값 + 1" 번호로 행을 추가할 때, 잠금 방식과 격리 수준 12가지 조합에서 번호가 겹치는지 재현 | `Kotlin` `PostgreSQL 16` `Testcontainers` |
| **[checkout-in-doubt](https://github.com/iohyeon/checkout-in-doubt)** | 결제 승인 결과를 알 수 없는 상태(in-doubt)를 PG 시뮬레이터로 만들고, 주문과 결제가 그 상태를 어떻게 처리하는지 확인 | `Java 21` `Spring Boot` `PG 시뮬레이터` |
| **[system-design-experiments](https://github.com/iohyeon/system-design-experiments)** | 시스템 설계 스터디에서 정한 숫자(prefix 캐시 크기, Redis fork 메모리, 업로드 블록 크기)를 직접 측정 | `Java` `Python` `Redis` |

## 프로젝트

| 저장소 | 무엇을 만들었나 | 기술 |
|---|---|---|
| **[chat-message-ordering](https://github.com/iohyeon/chat-message-ordering)** | 메시지 쓰는 서버가 교체될 때, 밀려난 이전 서버의 쓰기를 Kafka와 DB 중 어디서 막을지 직접 재현해 비교한 실험 | `Kafka 트랜잭션` `PostgreSQL` `Testcontainers` |
| **[payment-anomaly-platform](https://github.com/iohyeon/payment-anomaly-platform)** | 결제 기록에서 이상 패턴을 찾아 점수를 매기고, 높은 건만 따로 빼내는 구조 | `Spring Boot` `Kafka` `Outbox` `SKIP LOCKED` |
| **[llm-gateway](https://github.com/iohyeon/llm-gateway)** | 흩어진 LLM 호출을 한 군데로 모아 사용량과 비용을 같이 보는 중계 서버 | `Kotlin` `헥사고날` `WebFlux SSE` `BPE` |
| **[rag-qa-service](https://github.com/iohyeon/rag-qa-service)** | 문서를 찾아 답하고, 붙은 출처가 실제로 있는지 확인하는 QA 서비스. 검사 단계는 [hallucination-guard](https://github.com/iohyeon/hallucination-guard)로 분리 | `Go` `pgvector` `LLM-as-judge` |
| **[kafka-pipeline-lab](https://github.com/iohyeon/kafka-pipeline-lab)** | 유실과 중복 상황을 일부러 만들어보고 부하 테스트로 측정한 실습 | `Kafka KRaft` `Debezium` `k6` |
| **Saga 실험 2개** | [saga-microservices-lab](https://github.com/iohyeon/saga-microservices-lab): 계좌 이체가 중간에 실패했을 때의 보상, 타임아웃, 재시도<br>[kafka-eda-lab](https://github.com/iohyeon/kafka-eda-lab): 코레오그래피와 오케스트레이션의 보상 흐름과 결합도 비교 | `Java 21` `Kafka` `Saga` |

## 설계 기록

- [Outbox Relay 트레이드오프: 동기 Polling을 고른 이유](https://github.com/iohyeon/kafka-pipeline-lab/blob/main/docs/Outbox%20Relay%20%EC%B5%9C%EC%A2%85%20%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%93%9C%EC%98%A4%ED%94%84%20%E2%80%94%20%EB%8F%99%EA%B8%B0%20Polling%EC%9D%B4%20%EB%A7%9E%EB%8A%94%20%EC%9D%B4%EC%9C%A0.md)
- [부하테스트 실측 결과와 병목 분석](https://github.com/iohyeon/kafka-pipeline-lab/blob/main/docs/%EC%8B%AC%ED%99%94%20%E2%80%94%20%EB%B6%80%ED%95%98%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%8B%A4%EC%B8%A1%20%EA%B2%B0%EA%B3%BC%20%2B%20%EB%B3%91%EB%AA%A9%20%EB%B6%84%EC%84%9D.md)
- [채팅 메시지 순서 실험: 브로커 fencing과 저장소 fencing이 성립하는 조건](https://github.com/iohyeon/chat-message-ordering#findings)
- [논문 검색 설계 결정: 청크 크기, 필터 결합, 하이브리드 점수](https://github.com/iohyeon/pgvector-arxiv-search/blob/main/docs/DESIGN.md)
- [설계 결정 기록 6건](https://github.com/iohyeon/payment-anomaly-platform/tree/main/docs/decisions)

## 최근 블로그 글

<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->

[전체 글 보기](https://develop-tracking.tistory.com/)

## 스터디

**루프팩 BE L2**: 주차별 과제를 PR로 제출하고 멘토 코드리뷰를 받은 백엔드 심화 과정

- [loop-pack-be-l2-vol3-java](https://github.com/iohyeon/loop-pack-be-l2-vol3-java)
- [loop-pack-be-l2-vol2-java](https://github.com/iohyeon/loop-pack-be-l2-vol2-java)
- [loop-pack-be-l2-vol2-kotlin](https://github.com/iohyeon/loop-pack-be-l2-vol2-kotlin)

**북스터디와 실습**

- [system-design-study](https://github.com/iohyeon/system-design-study): 『가상 면접 사례로 배우는 대규모 시스템 설계 기초』 스터디
- [dev-book-study](https://github.com/iohyeon/dev-book-study): 『주니어 백엔드 개발자가 반드시 알아야 할 실무 지식』 스터디
- [spring-diy-1](https://github.com/iohyeon/spring-diy-1): Spring Framework 핵심 기능을 직접 구현하며 내부 동작 확인
- [pgvector-arxiv-search](https://github.com/iohyeon/pgvector-arxiv-search): PostgreSQL과 pgvector로 만든 논문 의미 검색
- [vector-search-experiments](https://github.com/iohyeon/vector-search-experiments): FAISS, SQLite, pgvector 벡터 검색 재현율 비교
- [sutskevers-list-study](https://github.com/iohyeon/sutskevers-list-study): AlexNet, ResNet, RNN, LSTM을 수식과 구현으로 다시 확인

## 활동

<img src="https://ghchart.rshah.org/iohyeon" alt="Contribution Chart" width="100%">
