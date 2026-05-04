# ORM과 데이터 영속성 정리

## SQL과 ORM의 차이

SQL은 개발자가 DB 테이블과 컬럼을 기준으로 조회 문장을 직접 작성하는 방식이다. ORM은 `Lion` 모델 같은 Python 클래스를 통해 데이터를 객체처럼 다루면 Django가 필요한 SQL로 변환해 DB와 통신하는 방식이다.

이 프로젝트에서는 SQL을 직접 작성하지 않고 다음 ORM 메서드로 데이터를 처리한다.

| 동작 | ORM |
| --- | --- |
| 생성 | `Lion.objects.create()` |
| 전체 조회 | `Lion.objects.all()` |
| 단건 조회 | `Lion.objects.get()` |
| 조건 조회 | `filter()` |
| 정렬 | `order_by()` |
| 개수 확인 | `count()` |
| 수정 | 필드 변경 후 `save()` |
| 삭제 | `delete()` |

## Lazy Loading이 필요한 이유

QuerySet은 단순 리스트가 아니라 조회 조건을 담고 있는 객체다. QuerySet을 만드는 순간 바로 DB를 조회하지 않고, 템플릿에서 순회하거나 `count()`, `list()`처럼 실제 결과가 필요한 시점에 쿼리가 실행된다.

Lazy Loading이 있으면 `filter()`, `order_by()` 같은 조건을 여러 단계로 조합한 뒤 최종적으로 필요한 쿼리만 실행할 수 있다. 그래서 불필요한 DB 접근을 줄이고, 검색/필터/정렬 조건을 더 유연하게 구성할 수 있다.

## 6주차, 7주차, 8주차 차이

| 항목 | 6주차 메모리 | 7주차 Model + DB | 8주차 ORM 이해 |
| --- | --- | --- | --- |
| 저장 위치 | 전역 리스트 | MySQL DB | MySQL DB |
| 데이터 유지 | 서버 종료 시 사라짐 | 서버 재시작 후 유지 | 서버 재시작 후 유지 |
| 데이터 단위 | `dict` | Model 인스턴스 | Model 인스턴스와 QuerySet |
| 조회 방식 | 리스트 순회 | 기본 ORM 조회 | `Q`, `filter()`, `get()`, `order_by()`, `count()` |
| 핵심 목표 | CRUD 흐름 경험 | Model/Admin/DB 적용 | ORM 동작 원리와 영속성 이해 |

8주차의 핵심은 DB를 직접 SQL로 다루는 것이 아니라, Model과 QuerySet을 통해 객체 중심으로 데이터를 조회하고 변경하는 흐름을 이해하는 것이다.
