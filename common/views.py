from django.shortcuts import render
from .models import Article


def test(request):
    articles = Article.objects.all()[:5]
    return render(request, 'common/test.html.jinja2', {'articles': articles})
