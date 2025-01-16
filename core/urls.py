from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio_app.urls")),
]

admin.site.site_title = "Portfolio CMS    \t\t\t @Yosef.E"
admin.site.site_header = "Yosef Emyayu"
