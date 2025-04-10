from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('news/', views.news_home, name='news_home'),
    path('news/<int:id>/', views.news_details, name='news-detail'),  # Изменили имя на 'news-detail'
    path('create/', views.create, name='create'),
    path('news/<int:id>/update/', views.news_update, name='news-update'),
    path('news/<int:id>/delete/', views.news_delete, name='news-delete'),
]