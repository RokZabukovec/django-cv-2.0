from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'project/(?P<pk>\d+)/$', views.project),
    url(r'projects$', views.projects),
    url(r'download$', views.download_pdf),
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)