from django.urls import path
from . import views

urlpatterns = [
    path("", views.dynamic_page, name="dynamic_page"),
    path("<str:page_name>", views.dynamic_page, name="dynamic_page"),
]
