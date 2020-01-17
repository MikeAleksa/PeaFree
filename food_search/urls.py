from django.urls import path

from . import views

app_name = 'food_search'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_num>/', views.detail, name='detail'),
    path('results/', views.results, name='results'),
]
