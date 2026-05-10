## 프로젝트 소개
- 프로젝트 목적: Django ORM과 MySQL을 활용한 아기사자 관리 시스템 구축
- 구현 기능 요약: Lion CRUD, Task 완료 토글, Tag 연동(N:M), 프로필 관리
- 사용 기술: Python, Django, MySQL, Django ORM

## 실행 방법
1. git clone <repository>
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver

## ERD 구조
- [cite_start]Lion (1) : Task (N) : ForeignKey, CASCADE 관계 [cite: 331, 341]
- [cite_start]Lion (1) : LionProfile (1) : OneToOneField, CASCADE 관계 [cite: 314, 328]
- [cite_start]Lion (N) : Tag (M) : ManyToManyField, 중간 테이블 자동 생성 [cite: 373, 374]

## 핵심 설계 설명
- [cite_start]연관관계: 유저의 활동(Task)과 신상(Profile)을 체계적으로 분리하여 관리하기 위해 FK와 OneToOne 사용. 
- [cite_start]트랜잭션: 새로운 사자 등록 시 관련 정보(Task, Profile)가 하나라도 실패하면 전체를 취소하여 데이터 무결성 유지. [cite: 435, 439]
- [cite_start]ORM 사용 이유: SQL 직접 작성 없이 객체 지향적으로 DB를 조작하여 생산성 증대 및 보안(SQL Injection 방지) 강화. [cite: 167]