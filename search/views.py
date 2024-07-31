from django.shortcuts import render
from common.models import Politician

# Create your views here.


def search(request):
    if request.htmx:
        print(request.GET.get('q', ''))
        query = request.GET.get('q', '')
        poli = Politician.objects.filter(name__icontains=query)
        print(poli[0].name, poli[0].organizations.all())

        context = {
            'search_results': {
                'politician': poli,
            }
        }
        return render(
            request,
            'search/components/search_results.html.jinja2',
            context
        )
    return render(request, 'search/search.html.jinja2')
