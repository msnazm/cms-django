from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index.as_view(), name="blog_index"),
    #path('', views.index, name='index'),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]