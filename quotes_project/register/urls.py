from django.urls import path
from quotes import views as quote_views

app_name = 'register'

urlpatterns = [
    path('', quote_views.register, name='register'),
]
