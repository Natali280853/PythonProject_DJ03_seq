from django.shortcuts import render

def home(request):
    return render(request, 'main/new.html')

# def index(request):
#     data = {
#         'caption': "ПОЗА ЛОТОСА"
#     }
#     return render(request, 'main/index.html', data)


def new(request):
    return render(request, 'main/new.html')
