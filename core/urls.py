from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),# ('') rota para raiz - IndexView.as_view() vai ser executada como uma função
    
]
