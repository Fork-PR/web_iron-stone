# API 명세서


1. [URL 문서](#URL-문서)
2. [API 문서](#API-문서)
3. [DB](#DB)

## URL 문서 

| URL               | 설명                                 |
| ----------------- | ------------------------------------ |
| /bobapps          | 기본 page url                        |
| /bobapps/login_page| 로그인 성공 시 이동되는 페이지     |
| /bobapps/save_menu|새로운 메뉴를 입력하면 데이터베이스에 저장하는 페이지|



## API 문서 

| API               |Method|설명 |
| ----------------- |------| ---------------------- |
| /bobapps/signup   |POST| 회원가입?? |
| /bobapps/user_login| POST| 로그인 인증결과 반환 |
| /bobapps/menuList |GET| 점심 메뉴 데이터 반환|


## DB

### Menu
| Name  | Type | Des |
| ------|------ |------|
| date            | Date  | 날짜 (YYYY-MM-DD 형식)                      |
| menu_course_type| Text  | 메뉴의 종류를 분류하는 데이터 (양식, 한식 등) |
| main_dish       | Text  | 주요 메인 메뉴 데이터                        |
| sub_menus       | List  | 서브 메뉴의 리스트                           |
### User
| Name  | Type | Des |
| ------|------ |------|
| username     | Text   | 사용자의 고유한 이름     |
| password     | Text   | 사용자의 비밀번호       |
| email        | Text   | 사용자의 이메일 주소    |
| first_name   | Text   | 사용자의 이름           |
| last_name    | Text   | 사용자의 성             |
| is_active    | Boolean| 사용자의 활성 여부      |
| is_staff     | Boolean| 사용자가 관리자 권한을 가지는지 여부 |
| is_superuser | Boolean| 사용자가 관리자로서 모든 권한을 가지는지 여부 |