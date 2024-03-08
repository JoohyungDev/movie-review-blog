from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("category/<str:slug>/", views.category_page),
    path("tag/<str:slug>/", views.tag_page),
]
