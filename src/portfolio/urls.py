
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index_view, name="home"),
    path('jobs/', include("jobs.urls", namespace="jobs")),
    path('studies/', include("studies.urls", namespace="studies")),
    path('contact/', views.contact_view, name="contact"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
