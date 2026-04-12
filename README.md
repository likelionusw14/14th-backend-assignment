# backend
# 🦁 멋쟁이사자처럼 수원대 14기 — Backend Session

## 과제 제출 방법
1. 이 레포를 **Fork**한다
2. `week{N}/본인이름/` 폴더에 과제 파일을 작성한다
3. 브랜치명: `이름/weekN` (예: `honggildong/week1`)
4. PR 제목: `[이름] weekN 과제 제출`
5. 마감: 매주 세션 전날 자정

## 폴더 구조
backend/
├── week1/   Python 기초 문법
├── week2/   Django 기초
└── ...

### 아기사자 과제 제출 플로우

**최초 1회 (1주차)**

```bash
# 1. Organization 레포 Fork
#    github.com/likelion-suwon-14th/backend → Fork 버튼

# 2. 내 계정으로 Clone
git clone https://github.com/본인계정/backend.git
cd backend

# 3. upstream 연결 (원본 레포 변경사항 받아오기 위해)
git remote add upstream https://github.com/likelion-suwon-14th/backend.git
```

**매주 반복**

```bash
# 1. upstream에서 최신 변경사항 받기 (새 주차 폴더 생겼을 때)
git fetch upstream
git merge upstream/main

# 2. 내 브랜치 생성
git checkout -b honggildong/week2

# 3. 내 폴더에 과제 작성
#    week2/홍길동/assignment1.py
#    week2/홍길동/assignment2.py

# 4. 커밋 & 푸시
git add .
git commit -m "feat: week2 과제 제출 - 홍길동"
git push origin honggildong/week2

# 5. GitHub에서 PR 생성
#    base: likelion-suwon-14th/backend:main
#    compare: 본인계정/backend:honggildong/week2
```
