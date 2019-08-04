from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls import url
from secondapp import views

urlpatterns = [
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
