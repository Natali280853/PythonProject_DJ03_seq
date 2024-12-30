from django.shortcuts import render
from .models import News_Post

def home(request):
    # Создаём переменную для получения всех записей.
    news = News_Post.objects.all()
    return render(request, 'news/news.html', {'news': news})

# def index(request):
#     data = {
#         'caption': "ПОЗА ЛОТОСА"
#     }
#     return render(request, 'main/index.html', data)
