from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path("<str:title>/", views.new_detail, name="new_detail"),
]