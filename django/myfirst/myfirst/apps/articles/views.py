from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    print(len(latest_articles))
    return render(request, 'articles/list.html', {'latest_articles': latest_articles})


def test(request):
    return HttpResponse('TestoTesto')


def detail(request, article_id:int):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена!")

    latest_comments = a.comment_set
    print(latest_comments)
    return render(request, 'articles/detail.html', {'article': a, 'comments': latest_comments})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)))

# Create your views here.
