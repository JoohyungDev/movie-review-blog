## 1. 목표와 기능
### 1.1 목표
- Python, Django Framework를 활용한 블로그 설계
- 기획 및 구현, 배포 사이클 경험
- 모놀리식 아키텍쳐 설계
- CBV(Class-Based View)
- WBS, ERD 설계 경험
- 문서화 경험
### 1.2 기능
- 공통
  - 토글 - 회원가입 / 로그인 버튼
  - 토글 메뉴 - 프로필 / 로그아웃
  - 검색
  - 카테고리, 해당 카테고리 목록 카운트
  - 홈버튼
- 메인 화면
  - 게시글 리스트
  - 게시글 작성
- 상세 화면
  - 해당 게시글 수정 및 삭제
  - 제목, 작성자, 조회수, 작성 시간, 수정 시간, 카테고리
  - 이미지, 본문, 파일 다운로드, 댓글 CRUD, 대댓글 CRUD
- 로그인 화면
  - 일반 로그인 / 구글 로그인
  - 회원가입
- 프로필 화면
  - 프로필 이미지 
  - 썸네일 이미지
  - 프로필 편집
- 프로필 편집 화면
  - 이름, 성, 닉네임, 프로필사진, 비밀번호 수정

### 1.3 팀 구성
- 개인 프로젝트

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
  - Web Framework
    - Django 5.0.3 (Python 3.11.7)
    - Bootstrap 5.3.1
  - 서비스 배포 환경
    - Amazon Lightsail
### 2.2 배포 URL
  - [URL](http://43.202.29.72:8000/blog/)
  - 관리자
    ```
    id : pjh
    pw : pjh1234!!
    ```
  - 일반 유저
    ```
    id : pjh1
    pw : pjh11234!!
    ```
  - 구글 로그인 유저
### 2.3 URL 구조(모놀리식)
- #### Config (main)
| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
|admin      |	'/admin/'	| -	|-	|관리자 화면|
|-	  |'/'	|RedirectView.as_view() |	-	|메인 화면 |
|blog	|'/blog/'	|-	|-	|blog.urls 내의 URL 패턴 참조|
|markdownx	|'/markdownx/'	|-	|-	| 본문 markdown 적용 |
|accounts	|'/accounts/'	|-	|-	| allauth |
|-	|'/media/'	|-	|-	|미디어 파일 접근을 위한 URL|


- #### Accounts (Django Allauth)

accounts 앱은 사용자 인증 및 관리를 위해 Django 프로젝트에 통합된 앱입니다. 이 앱은 django-allauth 패키지를 사용하여 구현되었으며, 사용자 로그인, 로그아웃, 회원가입, 소셜 로그인 등의 기능을 제공합니다. 이를 통해 사용자 경험(UX)을 대폭 향상합니다.

#### 기능
- 회원가입: 사용자는 이메일 주소, 아이디, 비밀번호를 사용하여 계정을 생성할 수 있습니다. 

- 로그인/로그아웃: 사용자는 아이디와 비밀번호를 사용하여 로그인할 수 있으며, 로그아웃도 가능합니다.

- 소셜 로그인: 페이스북, 구글, 트위터 등 여러 소셜 미디어 계정을 사용하여 로그인할 수 있습니다.

- 계정 관리: 사용자는 비밀번호 변경, 이메일 주소 추가 및 변경 등의 계정 관리 기능을 사용할 수 있습니다. 
  
- 비밀번호 재설정: 비밀번호를 잊은 사용자는 이메일을 통해 비밀번호를 재설정할 수 있습니다.


- #### Blog 


| App       | URL                                        | Views Function    | HTML File Name                        | Note           |
|-----------|--------------------------------------------|-------------------|---------------------------------------|----------------|
|blog	|'blog/'				|PostList.as_view()		|blog/post_list.html		|게시판 메인 화면|
|blog	|'blog/int:pk/'				|PostDetail.as_view()		|blog/post_detail.html		|상세 게시글 화면|
|blog	|'blog/category/str:slug/'		|category_page			|blog/post_list.html	        |카테고리별 게시글 보기|
|blog	|'blog/tag/str:slug/'			|tag_page			|blog/post_list.html		|태그별 게시글 보기|
|blog	|'blog/create_post/'			|PostCreate.as_view()		|blog/post_form.html		|게시글 작성|
|blog	|'blog/update_post/int:pk/'		|PostUpdate.as_view()		|blog/post_update_form.html	|게시글 수정|
|blog	|'blog/delete_post/int:pk/'		|PostDelete.as_view()		|blog/post_list.html   	        |게시글 삭제|
|blog	|'blog/search/str:q/'			|PostSearch.as_view()		|blog/post_list.html		|검색 기능|
|blog	|'blog/int:pk/create_comment/'		|create_comment			|blog/post_detail.html		|댓글 입력 폼|
|blog	|'blog/update_comment/int:pk/'		|CommentUpdate.as_view()	|blog/comment_form.html		|댓글 업데이트|
|blog	|'blog/delete_comment/int:pk/'		|delete_comment 		|blog/post_detail.html          |댓글 삭제|
|blog	|'blog/create_recomment/int:pk/'	|create_recomment		|blog/post_detail.html 	        |대댓글 입력 폼 |
|blog	|'blog/update_recomment/int:pk/'	|ReCommentUpdate.as_view()	|blog/recomment_form.html 	|대댓글 업데이트|
|blog	|'blog/delete_recomment/int:pk/'	|delete_recomment 		|blog/post_detail.html          |대댓글 삭제|
|blog	|'blog/profile/int:pk/'			|profile			|blog/profile.html		|프로필 보기|
|blog	|'blog/update_profile/int:pk/'		|ProfileUpdate.as_view()	|blog/profile_update.html	|프로필 업데이트|
|blog	|'blog/change_password/'		|ChangePassword.as_view()	|blog/change_password.html	|비밀번호 변경|

## 3. 기능 명세
```mermaid
graph TD
subgraph 비로그인
    A[메인 화면] --> B[게시글 목록];
    A --> C[게시글 검색];
    A --> D[카테고리별 게시글 목록];
    B --> E[게시글 세부 내용 조회];
    C --> E;
    D --> E;
end;
```

```mermaid
graph TD
subgraph login ["로그인 방식"]
    A1[일반 로그인] --> A[메인 화면]
    A2[구글 로그인] --> A
end

A --> F[프로필 화면]
A --> G[게시물 작성]

subgraph profile ["프로필"]
    F --> H[프로필 정보 수정]
    F --> I[비밀번호 변경]
end

subgraph post_content ["게시물"]
    G --> J[제목]
    G --> K[훅]
    G --> L[본문]
    G --> M[이미지]
    G --> N[카테고리]
    G --> O[태그]
end
```

```mermaid
graph TD
subgraph 로그인
    A[상세 화면] -->|본인 확인| B[게시글 수정/삭제 가능]
    A --> C[댓글 작성]
    C -->|본인 확인| D[댓글 수정/삭제 가능]
    C --> E[대댓글 작성]
    E -->|본인 확인| F[대댓글 수정/삭제 가능]
    A -->|공통| G[본문 조회]
    A -->|공통| H[댓글 조회]
    A -->|공통| I[태그 게시물 조회]
    A -->|공통| J[파일 다운로드]
end;
```
    
## 4. 프로젝트 구조와 개발 일정
### 4.1 프로젝트 구조
```
📦my-hobby-blog
 ┣ 📂accounts
 ┣ 📂blog
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📂blog
 ┃ ┃ ┃ ┣ 📂bootstrap
 ┃ ┃ ┃ ┃ ┣ 📂assets
 ┃ ┃ ┃ ┃ ┃ ┗ 📜favicon.ico
 ┃ ┃ ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┃ ┃ ┗ 📜styles.css
 ┃ ┃ ┃ ┃ ┣ 📂js
 ┃ ┃ ┃ ┃ ┃ ┗ 📜scripts.js
 ┃ ┃ ┃ ┃ ┗ 📜index.html
 ┃ ┃ ┃ ┗ 📂images
 ┃ ┃ ┃ ┃ ┗ 📜default_profile.png
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📂blog
 ┃ ┃ ┃ ┣ 📜base.html
 ┃ ┃ ┃ ┣ 📜base_full_width.html
 ┃ ┃ ┃ ┣ 📜comment_form.html
 ┃ ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┃ ┣ 📜post_form.html
 ┃ ┃ ┃ ┣ 📜post_list.html
 ┃ ┃ ┃ ┣ 📜post_update_form.html
 ┃ ┃ ┃ ┣ 📜profile.html
 ┃ ┃ ┃ ┣ 📜profile_update.html
 ┃ ┃ ┃ ┗ 📜recomment_form.html
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂config
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📂files
 ┃ ┃ ┃ ┗ 📂2024
 ┃ ┃ ┃ ┃ ┗ 📂03
 ┃ ┃ ┃ ┃ ┃ ┣ 📂07
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜test.xlsx
 ┃ ┃ ┃ ┃ ┃ ┗ 📂11
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜test.txt
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜test.xlsx
 ┃ ┃ ┗ 📂images
 ┃ ┃ ┃ ┣ 📂2024
 ┃ ┃ ┃ ┃ ┗ 📂03
 ┃ ┃ ┃ ┃ ┃ ┣ 📂07
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜자연이미지.jpg
 ┃ ┃ ┃ ┃ ┃ ┗ 📂11
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜자연이미지.jpg
 ┃ ┃ ┃ ┗ 📂thumbnail
 ┃ ┃ ┃ ┃ ┗ 📂2024
 ┃ ┃ ┃ ┃ ┃ ┗ 📂03
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂12
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜default_profile.png
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜보드와테이블.jpg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜석양과도시.jpg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜섬과바다.jpg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜자연이미지.jpg
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜햇빛이미지.jpg
 ┣ 📂templates
 ┃ ┣ 📂account
 ┃ ┣ 📂allauth
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```
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
    추가 기능 구현 :a6, 2024-03-10, 2024-03-14
    section 배포
    배포 :a7, 2024-03-12, 2024-03-14
    section 문서작업
    README 파일 수정 :a8, 2024-03-12, 2024-03-14

```

## 5. 와이어프레임 / UI
### 5.1 와이어프레임
<table>
    <tbody>
        <tr>
            <td>메인 화면</td>
            <td>상세 게시글 화면</td>
        </tr>
        <tr>
            <td>
		<img src="samples/wireframe/01_메인페이지.png" width="100%">
            </td>
            <td>
                <img src="samples/wireframe/02_세부페이지.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>카테고리 조회</td>
            <td>태그 조회</td>	
        </tr>
        <tr>
            <td>
                <img src="samples/wireframe/03_카테고리 조회.png" width="100%">
            </td>
            <td>
                <img src="samples/wireframe/04_태그 조회.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>게시글 작성</td>
            <td>게시글 수정</td>
        </tr>
        <tr>
            <td>
                <img src="samples/wireframe/05_포스트 작성.png" width="100%">
            </td>
            <td>
                <img src="samples/wireframe/06_포스트 수정.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>댓글</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
	        <img src="samples/wireframe/07_댓글.png" width="100%">
            </td>
            <td>
                <img src="samples/wireframe/08_로그인.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>회원가입</td>
            <td>아이디 찾기</td>
        </tr>
        <tr>
            <td>
                <img src="samples/wireframe/09_회원가입.png" width="100%">
            </td>
	    <td>
                <img src="samples/wireframe/10_아이디찾기.png" width="100%">
            </td>
        </tr>
	<tr>
            <td>비밀번호 찾기</td>
            <td>비밀번호 변경</td>
        </tr>
        <tr>
            <td>
                <img src="samples/wireframe/11_비밀번호찾기.png" width="100%">
            </td>
	    <td>
                <img src="samples/wireframe/12_비밀번호 변경.png" width="100%">
            </td>
        </tr>
 	<tr>
            <td>프로필</td>
            <td>프로필 수정</td>
        </tr>
        <tr>
            <td>
                <img src="samples/wireframe/13_프로필.png" width="100%">
            </td>
	    <td>
                <img src="samples/wireframe/14_프로필 수정.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

### 5.2 화면 설계
<table>
    <tbody>
        <tr>
            <td>메인 상단</td>
            <td>메인하단</td>
        </tr>
        <tr>
            <td>
		<img src="samples/product/메인상단.png" width="100%">
            </td>
            <td>
                <img src="samples/product/메인하단.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>상세 게시물</td>
            <td>카테고리 조회</td>	
        </tr>
        <tr>
            <td>
                <img src="samples/product/세부 페이지.png" width="100%">
            </td>
            <td>
                <img src="samples/product/카테고리 조회.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>태그 조회</td>
            <td>게시글 작성</td>
        </tr>
        <tr>
            <td>
                <img src="samples/product/태그 조회.png" width="100%">
            </td>
            <td>
                <img src="samples/product/게시글 작성.png" width="100%">
            </td>
        </tr>
        <tr>
           <td>게시글 수정</td>
           <td>댓글</td>
        </tr>
        <tr>
            <td>
	        <img src="samples/product/게시글 수정.png" width="100%">
            </td>
            <td>
                <img src="samples/product/댓글.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>로그인</td>
            <td>구글 로그인</td>
        </tr>
        <tr>
            <td>
                <img src="samples/product/로그인.png" width="100%">
            </td>
            <td>
                <img src="samples/product/구글 로그인.png" width="100%">
            </td>
        </tr>
	 <tr>
            <td>회원가입</td>
            <td>비밀번호 수정</td>
        </tr>
        <tr>
            <td>
                <img src="samples/product/회원가입.png" width="100%">
            </td>
	    <td>
                <img src="samples/product/비밀번호 찾기.png" width="100%">
            </td>
        </tr>
 	<tr>
            <td>프로필</td>
            <td>프로필 수정</td>
        </tr>
        <tr>
            <td>
                <img src="samples/product/프로필.png" width="100%">
            </td>
	    <td>
                <img src="samples/product/프로필 수정.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

## 6. 데이터베이스 모델링(ERD)
![ERD](https://github.com/JoohyungDev/my-hobby-blog/assets/113663639/86d96a27-c9a7-4426-a535-ba372265b4d9)

## 7. 트러블슈팅 및 개선
### 7.1 관리자 화면 레이아웃 오류
관리자 페이지의 기능들은 정상 작동하지만 레이아웃이 정상 출력되지 않는 오류가 발생하였습니다.
![image](https://github.com/JoohyungDev/my-hobby-blog/assets/113663639/1a5f4c97-eeea-4399-9a87-fc20b53b58a6)
![image](https://github.com/JoohyungDev/my-hobby-blog/assets/113663639/beff7897-153e-451c-a0b5-0fdc2576ea7b)

조사 결과, 해결책은 2가지가 있었습니다. 
1. Django 버전 다운그레이드
   - 5.0.3 -> 3.2.14로 낮춰서 해결이 가능합니다.
2. 캐시 제거
   - 관리자 화면에서 CTRL + SHIFT + R을 눌러 캐시를 제거하여 해결이 가능합니다.

### 7.2 IntegrityError 오류
```
IntegrityError at /post/new/ NOT NULL constraint failed: blog_post.author_id
```

게시글 생성 view를 만들고 나서 해당 URL로 폼을 작성하고 저장을 하니 위와 같은 오류가 발생하였습니다. <br>
CBV로 선언한 PostCreate 클래스 내부에 form_valid라는 폼을 검증하는 함수를 추가하여 author를 자동으로 추가하게끔 작성하여 해결하였습니다.
```
def form_valid(self, form):
    current_user = self.request.user
    if current_user.is_authenticated:
        form.instance.author = current_user
        return super(PostCreate, self).form_valid(form)
    else:
        return redirect("/blog/")
```

### 7.3 UNIQUE constraint failed 오류
```
UNIQUE constraint failed: blog_tag.slug
```
게시글 작성 시 태그를 태그1; 태그2 로 작성하면 정상 반영되지만 태그1; 태그2; 처럼 마지막을 세미콜론(;)으로 끝내면 위와 같은 오류가 발생하였습니다. <br>
일반적인 경우에서는 일어나지 않을 오류이지만 본인과 같은 실수를 예방하고자 view에서 PostCreate 클래스의 form_valid라는 폼 유효성 함수 내부에 다음과 같은 코드를 추가하여 해결하였습니다.
```
tags_str = tags_str.strip("; ")
```

### 7.4 게시글 삭제 관련 로직 단순화
![image](https://github.com/JoohyungDev/my-hobby-blog/assets/113663639/50668c85-b20e-4639-8265-eddf2aa380b9)
기존 코드는 게시글 세부 화면에서 삭제를 누르면 다른 페이지로 이동하여 삭제를 진행하였는데 이 과정에서 불편함을 느꼈으며 다음과 같이 수정하였습니다. 
```
<form class="post-form d-inline" action="{% url 'post_delete' post.pk %}"
method="post">
    {% csrf_token %}
    <a href="{% url 'post_delete' post.pk %}">
    <input type="submit" value="확인" class="btn btn-primary">
    </a>
</form>
```
확인 버튼을 form 태그로 감싸고 post_delete라는 이름의 삭제 클래스 URL과 연결 시켰습니다. 그 다음, views의 삭제 클래스 내부 get함수를 오버라이딩 하였습니다.
```
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
```
결과적으로 삭제 버튼을 누르는 즉시 삭제가 되며, 지연 시간을 50%이상 감소시켰습니다.

### 7.5 django-allauth 오류
```
allauth.account.middleware.AccountMiddleware must be added to settings.MIDDLEWARE
```
django-allauth를 활용한 소셜미디어 로그인 기능을 사용하고자 하였으나 위와 같은 문제가 발생하였습니다. <br>
settings.py 내부의 MIDDLEWARE 부분에 "allauth.account.middleware.AccountMiddleware"를 추가하여 간단히 해결하였습니다.

### 7.6 DB 오류
```
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration socialaccount.0001_initial is applied before its dependency sites.0001_initial
on database 'default'.
```
allauth를 세팅하며 settings.py를 수정중 문제가 발생하였습니다. 다른 앱들은 정상적으로 추가가 되지만 django.contrib.sites 앱을 후에 추가해주어 문제가 발생하였습니다. <br>
allauth를 활용한 소셜 로그인에는 sites를 admin페이지에서 수정해야 하는데 선언이 초기에 안되어 있었습니다. <br>
결국, 너무 늦게 선언을 하여 에러가 발생한 것입니다. <br>
조사 결과, 여러 해결방안이 나왔지만 해당되지 않았기에 migrations 폴더 전체와 db.sqlite3를 날려버리고 다시 재선언하였습니다.
#### 해결 순서
1. 해당 user model을 설정한 app의 migrations 폴더 제거
2. db.sqlite3 파일 삭제
3. python manage.py makemigrations <app 이름>
4. python manage.py migrate <app 이름>
5. python manage.py createsuperuser

### 7.7 WSGI 오류
```
'WSGIRequest' object has no attribute 'author'
```
포스트 상세 페이지에 댓글 기능을 추가하던 중, 위와 같은 오류가 발생했습니다. <br>
해석해보면 기본적으로 WSGIRequest 객체에는 author 속성이 없어서 발생하고 있습니다. <br>
댓글 생성 함수인 create_comment 내부 comment.author = request.author 구문을 comment.author = request.user로 수정하여 해결하였습니다.


## 8. 개발하며 느낀점
기본적인 블로그 구현부터 다양한 추가 기능 구현까지, 예상했던 것보다 훨씬 많은 시간이 소요되었습니다. 하지만 사전에 작성해둔 WBS(업무 분류 체계) 덕분에 보다 효율적으로 프로젝트를 진행할 수 있었습니다. 프로젝트를 진행하며 부족함을 느끼고, 조사하는 데 많은 시간을 할애한 것은 아쉬운 점으로 남습니다. 한 오류를 해결하면 마치 마법처럼 다른 오류가 등장하고, 그 오류를 해결하면 또 다시 새로운 오류가 발생하는 연속적인 과정이 힘들었지만, 해결 후에는 그만큼 큰 만족감과 배움이 있었습니다.
<br><br>
장고를 처음 다뤄보는 프로젝트였기에 막히는 부분이 많았고, 대단한 프로젝트는 아니지만 결국 해결하고 이렇게 문서화를 작성하고 있다는 사실에 큰 의미를 두고 싶습니다. 이 과정을 통해 '일단 시작이 반이다'라는 말이 결코 틀리지 않음을 깨달았고, 다양한 참고 자료의 존재를 알게 되었습니다. 비교적 쉽게 문제를 해결할 수 있었던 지금의 저는 새로운 길을 개척했던 선배 개발자들의 노력에 깊은 존경심을 느낍니다. 항상 부족함을 느끼며 겸손하게 지식을 습득하고, 어려움을 겪고 있는 다른 개발자들에게 도움을 주는 개발자가 되고자 합니다.

