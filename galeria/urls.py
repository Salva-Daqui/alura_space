from django.urls import path
from galeria import views

urlpatterns = [ 
    path('', views.index, name = 'home'),
    path('imagem/', views.img, name = 'imagem'),
]