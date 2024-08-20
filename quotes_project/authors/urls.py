from django.urls import path
from . import views

app_name = 'authors'  # Додаємо app_name, щоб використовувати іменовані маршрути

urlpatterns = [
    path('', views.author_list, name='author_list'),  # Головна сторінка, список всіх авторів
    path('author/<int:pk>/', views.author_detail, name='author_detail'),  # Детальний перегляд автора
    path('author/new/', views.author_new, name='add_author'),  # Додати нового автора
    path('author/<int:pk>/edit/', views.author_edit, name='author_edit'),  # Редагувати автора
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),  # Видалити автора
]
