from django.shortcuts import render
from common.models import Article, Politician

# Create your views here.


def home(request):
    articles = Article.objects.all()[:5]
    article_list = {}
    # profile_category = request.GET.get('category', 'politician')

    if len(articles) <= 0:
        article_list = {
            'mainArticle': None,
            'articles': [],
        }
    else:
        article_list = {
            'mainArticle': articles[0],
            'articles': articles[1:],
        }

    context = {
        'article_list': article_list,
        'popular': {
            'profiles': Politician.objects.all().order_by('-views')[:10],
            'category': 'politician',
        }
    }

    if request.htmx and request.GET.get('HX-Target') == 'popularItems':
        return render(
            request,
            'home/components/popular_items.html.jinja2',
            context
        )
    return render(request, 'home/home.html.jinja2', context)
