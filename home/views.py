from django.shortcuts import render
from common.models import Article

# Create your views here.


def home(request):
    articles = Article.objects.all()[:5]
    context = {
        'article_list': {
            'bigArticle': articles[0],
            'articles': articles[1:],
        }
    }
    return render(request, 'home/home.html.jinja2', context)
