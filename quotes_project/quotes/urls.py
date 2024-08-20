from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.quote_list, name='index'),  # Змінено ім'я на 'index'
    path('quote/<int:pk>/', views.quote_detail, name='quote_detail'),
    path('quote/new/', views.quote_new, name='add_quote'),
    path('quote/<int:pk>/edit/', views.quote_edit, name='quote_edit'),
    path('quote/<int:pk>/delete/', views.quote_delete, name='quote_delete'),
    path('tag/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),  # Додано шлях для фільтрації за тегом
]
