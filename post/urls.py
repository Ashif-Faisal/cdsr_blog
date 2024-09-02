from django.urls import path
from .views import HomePage, DetailsView, CreatePost, DeletePost, UpdatePost

urlpatterns = [
    path("", HomePage.as_view(),name="home"),
    path("<int:pk>/", DetailsView.as_view(), name="DetailsView"),
    path("newpost/", CreatePost.as_view(), name="newpost"),
    path("delete/<int:pk>/", DeletePost.as_view(), name="delete"),
    path("update/<int:pk>/", UpdatePost.as_view(), name="update")
]