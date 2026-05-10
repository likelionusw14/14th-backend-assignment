# 아기사자 관리 서비스

## 1. 프로젝트 소개
### 프로젝트 목적
- Django 실습
- 트랜잭션의 이해

### 구현 기능 요약
- 사자 관리: 목록 조회, 검색, 생성, 수정, 삭제
- 과제 관리: 사자당 기본 과제 3개 자동 생성 및 완료 여부 토글
- 프로필 관리: 상세 정보 수정 및 조회
- 태그 관리: 관심 분야 키워드 추가 및 제거

### 사용 기술
- Python
- Django
- MySQL
- Django ORM

## 2. 실행 방법
git clone <repository_url>
cd pbl10

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

## 3. ERD 구조
- Lion (1) : Task (N) : ForeignKey, CASCADE
- Lion (1) : LionProfile (1) : OneToOneField, CASCADE
- Lion (N) : Tag (M) : ManyToManyField, 중간 테이블 자동 생성

## 4. 핵심 설계 설명
### 1:N / 1:1 / N:M 관계 설계 이유
정보를 깔끔하게 관리하려고 사자 기본 정보와 프로필을 1:1로 나눴다. 사자 한 명에게 여러 과제를 붙여주려고 1:N 관계를 썼고, 사자를 지우면 과제도 같이 삭제되게 만들었다. 태그는 여러 사자가 키워드를 같이 쓸 수 있도록 N:M 관계를 활용해 유연하게 구현했다.

### transaction.atomic() 적용 이유
사자를 만들 때 프로필이랑 과제까지 한 번에 다 생겨야 해서 트랜잭션을 썼다. 하나라도 생기다 오류 나면 전체를 취소하도록 만들어서, 이름만 저장되고 과제는 안 나오는 식의 데이터 꼬임 문제를 막고 신뢰성을 높였다.

### ORM만 사용한 이유
SQL을 직접 안 짜고 파이썬 코드로 데이터를 다룰 수 있어 코딩이 편하고 속도도 빨랐다. 직접 쿼리를 쓰면 생길 수 있는 보안 문제를 막아주고, 나중에 DB를 바꿔도 코드를 거의 안 고쳐도 되는 장점 때문에 ORM을 선택했다.