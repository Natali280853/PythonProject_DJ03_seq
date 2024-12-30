from django.shortcuts import render
from models import News_Post
from .forms import NewsPostForm


def home(request):
    # Создаём переменную для получения всех записей.
    news = News_Post.objects.all()
    return render(request, 'news/news.html', {'news': news})


def create_news(request):
    # Создаём переменную для получения всех записей.
    form = NewsPostForm()
    return render(request, 'news/add_new_post.html', {'form': form})

# def index(request):
#     data = {
#         'caption': "ПОЗА ЛОТОСА"
#     }
#     return render(request, 'main/index.html', data)
