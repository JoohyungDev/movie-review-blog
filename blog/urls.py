from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    path("category/<str:slug>/", views.category_page, name="category_page"),
    path("tag/<str:slug>/", views.tag_page, name="tag_page"),
    path("create_post/", views.PostCreate.as_view(), name="post_create"),
    path("update_post/<int:pk>/", views.PostUpdate.as_view(), name="post_update"),
    path("delete_post/<int:pk>/", views.PostDelete.as_view(), name="post_delete"),
    path("search/<str:q>/", views.PostSearch.as_view(), name="search"),
    path("<int:pk>/create_comment/", views.create_comment, name="comment_create"),
    path(
        "update_comment/<int:pk>/", views.CommentUpdate.as_view(), name="comment_update"
    ),
    path("delete_comment/<int:pk>/", views.delete_comment, name="comment_delete"),
    path(
        "create_recomment/<int:pk>/",
        views.create_recomment,
        name="recomment_create",
    ),
    path(
        "update_recomment/<int:pk>/",
        views.ReCommentUpdate.as_view(),
        name="recomment_update",
    ),
    path("delete_recomment/<int:pk>/", views.delete_recomment, name="recomment_delete"),
    path(
        "profile/<int:pk>/",
        views.profile,
        name="profile",
    ),
    path(
        "update_profile/<int:pk>/",
        views.ProfileUpdate.as_view(),
        name="profile_update",
    ),
    path(
        "change_password/",
        views.ChangePassword.as_view(),
        name="password_change",
    ),
]
