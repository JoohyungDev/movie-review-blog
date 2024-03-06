# 취미 블로그
## 1. 목표와 기능
### 1.1 목표
- 다양한 기능 구현
- Django와 친해지기
### 1.2 기능
- 기본적인 CRUD
- 로그인 / 회원가입
- 회원 관련 추가 기능
- 댓글 기능
- 간편 로그인 기능
### 1.3 팀 구성
- 개인 프로젝트

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
  - Web Framework
    - Django 5.0.2 (Python 3.12.1)
  - 서비스 배포 환경
    - Amazon Lightsail
### 2.2 배포 URL
  - URL
  - 테스트용 계정
    ```
    id : test@gmail.com
    pw : test1234!!
    ```
### 2.3 URL 구조(모놀리식)
- main

| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| main      | '/'                                        | home              | main/home.html                        | 홈화면          |
| main      | '/about/'                                  | about             | main/about.html                       | 소개화면               |


- accounts

| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| accounts  | 'signup/'                                  | signup          | accounts/signup.html                |회원가입         |
| accounts  | 'login/'                                   | login             | accounts/login.html                   |로그인           |
| accounts  | 'logout/'                                  | logout            | accounts/logout.html                  |로그아웃         |
| accounts  | 'profile/'                                 | profile           | accounts/profile.html                 | 비밀번호변경기능 / <br>프로필 수정/ 닉네임추가 |


- blog


| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
| blog      | 'blog/'                                    | blog_list          | blog/blog_list.html                        |갤러리형 게시판 메인 화면  |
| blog      | 'blog/<int:pk>/'                           | blog_detail        | blog/blog_detail.html                        |상세 포스트 화면    |
| blog      | 'blog/write/'                              | blog_create        | blog/blog_create.html                       | 카테고리 지정, 사진업로드,<br> 게시글 조회수 반영|
| blog      | 'blog/edit/<int:pk>/'                      | blog_update       | blog/blog_update.html                        | 게시물목록보기 |
| blog      | 'blog/delete/<int:pk>/'                    | blog_delete       | blog/delete.html                      | 삭제 화면      |
| blog      | 'blog/search/'                             | search            | blog/search.html                      | 주제와 카테고리에 따라 검색,<br> 시간순에 따라 정렬|
| blog      | 'post/<int:post_pk>/comment/'              | comment_new       | blog/comment_form.html                | 댓글 입력 폼     |
| blog      | 'post/<int:post_pk>/comment/<br><int:parent_pk>/' | reply_new    | blog/comment_form.html                | 대댓글 폼      |
| blog      | 'post/<int:pk>/like/'                      | like_post         | blog/post.html                        |좋아요를 누르면 blog/post로 Redirect됨|
| blog      | 'comment/<int:pk>/update/'                 | comment_update    | blog/comment_form.html                |댓글 업데이터 경로   |
| blog      | 'comment/<int:pk>/delete/'                 | comment_delete    | blog/comment_<br>confirm_delete.html      |댓글 삭제 폼    |


## 3. 요구사항 명세와 기능 명세

## 4. 프로젝트 구조와 개발 일정
### 4.1 프로젝트 구조
### 4.2 WBS
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title Django 영화리뷰 블로그 개발 일정
    section 기획
    아이디어 기획 :a1, 2024-03-05, 2024-03-07
    와이어프레임 & ERD :a2, 2024-03-06, 2024-03-07
    section 개발
    URL 구현 & 모델 구현 :a3, 2024-03-07, 2024-03-09
    CRUD 구현 :a4, 2024-03-08, 2024-03-10
    인증 구현 :a5, 2024-03-09, 2024-03-11
    추가 기능 구현 :a6, 2024-03-10, 2024-03-12
    section 배포
    배포 :a7, 2024-03-11, 2024-03-13
    section 문서작업
    README 파일 수정 :a8, 2024-03-12, 2024-03-13

```

## 5. 와이어프레임 / UI
### 5.1 와이어프레임
<table>
    <tbody>
        <tr>
            <td>메인</td>
            <td>세부페이지</td>
        </tr>
        <tr>
            <td>
		<img src="samples/01_대문.png" width="100%">
            </td>
            <td>
                <img src="samples/02_세부페이지.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>About 페이지</td>
            <td>글쓰기</td>
        </tr>
        <tr>
            <td>
                <img src="samples/03_about페이지.png" width="100%">
            </td>
            <td>
                <img src="samples/04_포스트 작성.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>수정</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
                <img src="samples/05_포스트 수정.png" width="100%">
            </td>
            <td>
                <img src="samples/06_로그인.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>비밀번호찾기</td>
            <td>아이디찾기</td>
        </tr>
        <tr>
            <td>
	        <img src="samples/07_비밀번호찾기.png" width="100%">
            </td>
            <td>
                <img src="samples/08_아이디찾기.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>회원가입</td>
        </tr>
        <tr>
            <td>
                <img src="samples/09_회원가입.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

### 5.2 화면 설계

## 6. 데이터베이스 모델링(ERD)
```mermaid
erDiagram
    user ||--o{ post : write
    user {
      integer id PK
      varchar username
      varchar password
      image profile_image
      datetime created_at
      varchar ip_address
      datetime last_login
    }
    post }|--|{ tag : contains
    post ||--o| category : has
    post {
      integer id PK
      varchar title
      text content
      file file_upload
      image image_upload
      datetime created_at
      datetime updated_at
      varchar writer
      integer user_id FK
      integer hits
      integer tags FK
      varchar category FK
    }
    post ||--o{ comment : contains
    comment ||--o{ comment : contains
    comment {
      integer id PK
      integer parent FK
      text comment
      comment comment_reply FK
      datetime created_at
      datetime updated_at
    }
    
    tag {
      integer id PK
      varchar name
    }
    
    
    category {
      integer id PK
      varchar name
    }
```
