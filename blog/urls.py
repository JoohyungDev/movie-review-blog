from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("category/<str:slug>/", views.category_page),
    path("tag/<str:slug>/", views.tag_page),
    path("create_post/", views.PostCreate.as_view()),
    path("update_post/<int:pk>/", views.PostUpdate.as_view()),
    path("delete_post/<int:pk>/", views.PostDelete.as_view(), name="post_delete"),
    path("search/<str:q>/", views.PostSearch.as_view()),
    path("<int:pk>/new_comment/", views.new_comment),
    path("update_comment/<int:pk>/", views.CommentUpdate.as_view()),
    path("delete_comment/<int:pk>/", views.delete_comment),
    path(
        "change_password/",
        views.ChangePassword.as_view(),
        name="password_change",
    ),
    # path("profile/<int:pk>/", views.UserProfile.as_view(), name="profile"),
    path(
        "profile/<int:pk>/",
        views.ProfileDetail.as_view(),
        name="profile",
    ),
]
