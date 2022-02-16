from . import views
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.PageViewFull.as_view(), name='base'),
    #path("new/<int:pk>/", views.news_detail, name="new_detail"),
    path("about/", views.aboutus, name="aboutus"),
    path("contact/", views.contact, name="contact"),

]