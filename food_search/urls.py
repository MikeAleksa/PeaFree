from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_num>/', views.detail, name='detail'),
    path('results/', views.results, name='results'),
    path('about/', views.about, name='about'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]