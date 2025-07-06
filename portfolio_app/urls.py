from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="landing"),
    path("contact/", views.contact, name="contact"),
    path("project_detail/<str:slug>/", views.project_detail, name="project_detail"),
    path("home/", views.home, name="home"),
    path("download-resume/", views.download_latest_resume, name="download_resume"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
