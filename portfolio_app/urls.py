from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings

from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("about/", views.about, name="about"),
    path("education/", views.education, name="education"),
    path("experience/", views.experience, name="experience"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
    # path("message/", views.message, name="contact"),
    path("flowbit/", views.flowbit, name="flowbit"),
    path("project_detail/<str:slug>/", views.project_detail, name="project_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
