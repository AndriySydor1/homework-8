from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from quotes import views as quotes_views  # Імпортуємо наші views з додатку quotes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', include('authors.urls')),  # Додаємо маршрути для додатку authors
    path('quotes/', include('quotes.urls')),  # Додаємо маршрути для додатку quotes
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Додаємо маршрут для входу
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Додаємо маршрут для виходу
    path('register/', quotes_views.register, name='register'),  # Додаємо маршрут для реєстрації
    path('', RedirectView.as_view(url='/authors/', permanent=False)),  # Перенаправлення на сторінку авторів
]
