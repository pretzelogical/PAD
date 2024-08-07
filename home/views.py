from django.shortcuts import render
from common.models import Article, Politician, Organization

# Create your views here.


def home(request):
    articles = Article.objects.all()[:5]
    article_list = {}
    popular_category = request.GET.get('popular', 'politician')
    popular = {}

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

    if popular_category == 'politician':
        popular = {
            'profiles': Politician.objects.all().order_by('-views')[:10],
            'category': popular_category,
        }
    else:
        popular = {
            'profiles': Organization.objects.all().order_by('-views')[:10],
            'category': popular_category,
        }

    context = {
        'article_list': article_list,
        'popular': popular
    }

    if request.htmx and request.htmx.target == 'popularItems':
        return render(
            request,
            'home/components/popular_items.html.jinja2',
            context
        )
    return render(request, 'home/home.html.jinja2', context)
