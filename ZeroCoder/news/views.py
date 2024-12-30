from django.shortcuts import render, redirect
from .models import News_Post
from .forms import NewsPostForm


def home(request):
    # Создаём переменную для получения всех записей.
    news = News_Post.objects.all()
    return render(request, 'news/news.html', {'news': news})


def create_news(request):
    # когда нажимаем на кнопку, работает метод POST (добавляем проверку на метод). Переменную error размещаем выше, чтобы она изначально имела пустое значение.
    error = ''
    if request.method == 'POST':
        form = NewsPostForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('news_home')   # из urls.py
        else:
            error = "Данные были заполнены некорректно"
    form = NewsPostForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})

# def index(request):
#     data = {
#         'caption': "ПОЗА ЛОТОСА"
#     }
#     return render(request, 'main/index.html', data)
