from django.shortcuts import render
from common.models import Politician, Organization
from django.http import HttpResponseBadRequest

# Create your views here.


def search(request):
    """ Search for either a politician or an organization """
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'politician')

    if category == 'politician':
        poli = Politician.objects.filter(name__icontains=query)
        context = {
            'search_results': {
                'politician': poli,
            }
        }

    if category == 'organization':
        org = Organization.objects.filter(name__icontains=query)
        context = {
            'search_results': {
                'organization': org,
            }
        }

    if request.htmx:
        return render(
            request,
            'search/components/search_results.html.jinja2',
            context
        )

    return render(request, 'search/search.html.jinja2', context)
