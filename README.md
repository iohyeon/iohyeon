<h1 align="center">Nahyeon Lim</h1>
<p align="center">Backend Developer</p>

<p align="center">
  <a href="https://develop-tracking.tistory.com/"><img src="https://img.shields.io/badge/Tech%20Blog-FF5A4A?style=for-the-badge&logo=tistory&logoColor=white" alt="Tech Blog"></a>
  <a href="https://www.linkedin.com/in/na-hyeon/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:iohyeonsz@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a>
</p>

## 🔭 Intro

요청이 몰리고 작업이 중간에 실패해도, 데이터가 어긋나지 않고 다시 복구할 수 있는 서버를 만듭니다.

- 결제·정산 시스템의 데이터 정합성과 상태 전이를 설계합니다.
- 비동기 파이프라인의 중복, 유실, 재처리 시나리오를 검증합니다.
- 성능과 AI 응답 품질을 감각이 아닌 측정과 자동화된 검증으로 확인합니다.

## ⚡ Stack

<img src="https://skillicons.dev/icons?i=java,kotlin,go,python,spring,kafka,rabbitmq,redis&perline=8" alt="Stack">
<br>
<img src="https://skillicons.dev/icons?i=mysql,postgres,mongodb,elasticsearch,docker,kubernetes&perline=6" alt="Stack">

## 📦 Projects

| Repository | 무엇을 만들었나 | 스택 |
|---|---|---|
| **[chat-message-ordering](https://github.com/iohyeon/chat-message-ordering)** | 메시지 쓰는 서버가 교체될 때, 밀려난 이전 서버의 쓰기를 Kafka와 DB 중 어디서 막을지 직접 재현해 비교한 실험 | `Kafka 트랜잭션` `PostgreSQL` `Testcontainers` |
| **[payment-anomaly-platform](https://github.com/iohyeon/payment-anomaly-platform)** | 결제 기록에서 이상 패턴을 찾아 점수를 매기고, 높은 건만 따로 빼내는 구조 | `Spring Boot` `Kafka` `Outbox` `SKIP LOCKED` |
| **[llm-gateway](https://github.com/iohyeon/llm-gateway)** | 흩어진 LLM 호출을 한 군데로 모아 사용량과 비용을 같이 보는 중계 서버 | `Kotlin` `헥사고날` `WebFlux SSE` `BPE` |
| **[hallucination-guard](https://github.com/iohyeon/hallucination-guard)** | LLM이 지어낸 답을 코드로 걸러보는 다단계 검사 파이프라인 | `Go` `인용 검증` `LLM-as-judge` |
| **[rag-qa-service](https://github.com/iohyeon/rag-qa-service)** | 문서를 찾아 답하고, 붙은 출처가 실제로 있는지 확인하는 QA 서비스 | `Go` `pgvector` `임베딩 사이드카` |
| **[pgvector-arxiv-search](https://github.com/iohyeon/pgvector-arxiv-search)** | 논문 본문을 잘게 나눠 의미로 찾고, 키워드 검색과 섞어 결과를 정확도로 확인한 검색 시스템 | `Python` `pgvector` `HNSW` `하이브리드 검색` |
| **[kafka-pipeline-lab](https://github.com/iohyeon/kafka-pipeline-lab)** | 유실과 중복 상황을 일부러 만들어보고 부하테스트로 재본 실습 | `Kafka KRaft` `Debezium` `k6` |
| **[saga-microservices-lab](https://github.com/iohyeon/saga-microservices-lab)** | 여러 서비스를 거치는 작업이 중간에 실패했을 때 되돌리는 실험 | `Java 21` `Saga` `Testcontainers` |

## 📐 설계 기록

- [Outbox Relay 트레이드오프: 동기 Polling을 고른 이유](https://github.com/iohyeon/kafka-pipeline-lab/blob/main/docs/Outbox%20Relay%20%EC%B5%9C%EC%A2%85%20%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%93%9C%EC%98%A4%ED%94%84%20%E2%80%94%20%EB%8F%99%EA%B8%B0%20Polling%EC%9D%B4%20%EB%A7%9E%EB%8A%94%20%EC%9D%B4%EC%9C%A0.md)
- [부하테스트 실측 결과와 병목 분석](https://github.com/iohyeon/kafka-pipeline-lab/blob/main/docs/%EC%8B%AC%ED%99%94%20%E2%80%94%20%EB%B6%80%ED%95%98%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%8B%A4%EC%B8%A1%20%EA%B2%B0%EA%B3%BC%20%2B%20%EB%B3%91%EB%AA%A9%20%EB%B6%84%EC%84%9D.md)
- [채팅 메시지 순서 실험: 브로커 fencing과 저장소 fencing이 성립하는 조건](https://github.com/iohyeon/chat-message-ordering#findings)
- [논문 검색 설계 결정: 청크 크기, 필터 결합, 하이브리드 점수](https://github.com/iohyeon/pgvector-arxiv-search/blob/main/docs/DESIGN.md)
- [설계 결정 기록 6건](https://github.com/iohyeon/payment-anomaly-platform/tree/main/docs/decisions)

## 📚 Study

**루프팩 BE L2** &nbsp;주차별 과제를 PR로 제출하고 멘토 코드리뷰를 받는 백엔드 심화 과정

[![vol3](https://img.shields.io/badge/vol3--java-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/loop-pack-be-l2-vol3-java)
[![vol2-java](https://img.shields.io/badge/vol2--java-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/loop-pack-be-l2-vol2-java)
[![vol2-kotlin](https://img.shields.io/badge/vol2--kotlin-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/loop-pack-be-l2-vol2-kotlin)
[![coding-test](https://img.shields.io/badge/coding--test--challenge2-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/loopers-coding-test-challenge2)

**북스터디와 랩**

[![system-design](https://img.shields.io/badge/system--design--study-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/system-design-study)
[![dev-book](https://img.shields.io/badge/dev--book--study-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/dev-book-study)
[![spring-diy](https://img.shields.io/badge/spring--diy--1-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/spring-diy-1)
[![kafka-eda](https://img.shields.io/badge/kafka--eda--lab-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/kafka-eda-lab)
[![vector-search](https://img.shields.io/badge/vector--search--experiments-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/vector-search-experiments)
[![sutskever](https://img.shields.io/badge/sutskevers--list--study-2b3137?style=flat-square&logo=github&logoColor=white)](https://github.com/iohyeon/sutskevers-list-study)

## 📊 Activity

<img src="https://ghchart.rshah.org/iohyeon" alt="Contribution Chart" width="100%">
