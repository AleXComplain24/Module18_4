from django.shortcuts import render

# Create your views here.

def platform_view(request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    games = {
        'Atomic Heart': 500,
        'Cyberpunk 2077': 800,
        'PayDay 2': 1200,
    }
    return render(request, 'third_task/games.html', {'games': games})

def cart_view(request):
    return render(request, 'third_task/cart.html')