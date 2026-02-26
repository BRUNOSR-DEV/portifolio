from django.urls import path
from django.contrib import admin

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),# ('') rota para raiz - IndexView.as_view() vai ser executada como uma função
    
]

admin.AdminSite.site_header = 'Administração'
admin.AdminSite.site_title = 'Portifólio'
admin.AdminSite.index_title = 'Área Administrativa|Portifólio'

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)