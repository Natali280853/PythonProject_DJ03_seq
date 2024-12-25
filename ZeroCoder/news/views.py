from django.shortcuts import render

def home(request):
    return render(request, 'news/news.html')

# def index(request):
#     data = {
#         'caption': "ПОЗА ЛОТОСА"
#     }
#     return render(request, 'main/index.html', data)
