# 급식알리미

## 과제 개요

점심은 든든하게!  
오늘의 점심메뉴를 확인하자

## 참여 인원

|Backend|Frontend| 
|:----:|:----:|
|최성철|최홍석|
|[@CSchoice](https://github.com/CSchoice)|[@k-redstone](https://github.com/k-redstone)|

## 실행 환경

 - python 3.9.13


## TECH
 ### Backend

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"/>

### Frontend

  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/><img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"/><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"/>




## 사용 방법
```python
# 1. 가상환경에서 필수 라이브러리 설치
pip install -r requirements.txt

# 2. DB 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 3. 서버 실행
python manage.py runserver

# 4. Root Url
localhost:8000/bobapps

```


## 주요 기능

### Frontend
- 페이지 디자인
- addEventListener()로 페이지 로딩시 식단리스트 요청
- form을 이용해 로그인 시 POST요청으로 로그인 정보를 보내고, 응답결과를 처리

### Backend



## 문서
 - [Commit 컨벤션](./docs/GIT_convention)
 - [API 명세서](./docs/API_DOCS)



<br/>

## 필수 구현사항

### 공통
- 본 과제는 **페어 프로그래밍**으로 작업을 진행해 주세요.
    - 둘 중 한명의 레포지토리를 다른 사람이 fork해가는 방식으로 해주시면 됩니다.
- 작업이 끝나면 커밋을 진행해주세요. 커밋 메시지에 대해 신경써보고, 커밋의 단위는 본인이 생각하는 최소 작업 단위로 구성해 주세요.

### FE
- django의 templates 폴더에 화면을 구성해 주세요.
- 바닐라 HTML/CSS를 활용하여 아래 figma에 디자인된 2개 페이지와 비슷하게 구성해 주세요.
    - 라이브러리를 사용할 경우(CDN) 그 이유를 README에 작성해 주세요.
- 최상단 폴더에 README.md를 구성하고 소개해 주세요.
- 페어와 의논해서 첫 페이지 로딩 시 우측 컨테이너에 급식 정보를 로딩시켜 보세요.
    - 데이터 형식은 자유롭게 정하셔도 됩니다.

### BE

- Django의 MTV 패턴을 활용하여 급식정보를 반환해야 합니다.
- form action request에 대해 적절한 페이지로 id, password를 response로 보내주세요.
- 최상단 폴더에 README.md를 구성해 주세요
- API 명세를 작성해 주세요.


## 선택 구현사항

### FE

- 로그인 버튼을 누르면 login 페이지로 이동되도록 구성해 보세요.
- index page input field에 담긴 정보가 로그인 화면에 나오게 구성해 보세요.

### BE

- 로그인 input에 대해 정규표현식으로 검사해 보세요.
- 모델 간 N:M 관계 구성
- Pagination과 Filter
