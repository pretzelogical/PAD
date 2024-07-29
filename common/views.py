from django.shortcuts import render


def test(request):
    return render(request, 'common/test.html.jinja2')
