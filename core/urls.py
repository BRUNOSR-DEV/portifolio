from django.urls import path
from django.contrib import admin

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),# ('') rota para raiz - IndexView.as_view() vai ser executada como uma função
    
]

admin.AdminSite.site_header = 'Administração'
admin.AdminSite.site_title = 'Portifólio'
admin.AdminSite.index_title = 'Área Administrativa|Portifólio'
