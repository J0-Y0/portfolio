from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings


urlpatterns = [
    path("", views.dynamic_page, name="dynamic_pages"),
    path("message/", views.message, name="message"),
    # path("<str:page_name>", views.dynamic_page, name="dynamic_page"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
