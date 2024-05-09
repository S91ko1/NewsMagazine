from django.shortcuts import render
from .models import News


def news_list(request):
    news = News.objects.all().order_by('-publication_date')  # ME-- Сортировка по убыванию даты
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, news_id):
    article = News.objects.get(id=news_id)
    return render(request, 'news_detail.html', {'article': article})
