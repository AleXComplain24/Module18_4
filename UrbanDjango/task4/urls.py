from django.urls import path
from .views import platform_view, games_view, cart_view

urlpatterns = [
    path('', platform_view, name='platform'),  # Главная страница
    path('games/', games_view, name='games'),  # Страница "Магазин"
    path('cart/', cart_view, name='cart'),     # Страница "Корзина"
]