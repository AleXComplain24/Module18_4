from django.shortcuts import render

# Главная страница
def platform_view(request):
    return render(request, 'fourth_task/platform.html')

# Магазин
def games_view(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'fourth_task/games.html', context)

# Корзина
def cart_view(request):
    return render(request, 'fourth_task/cart.html')