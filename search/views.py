from django.shortcuts import render
from common.models import Politician, Organization


def search(request):
    """ Search for either a politician or an organization """

    def create_context():
        query = request.GET.get('q', '')
        category = request.GET.get('category', 'politician')
        page = int(request.GET.get('page', 0))
        PAGE_SIZE = 3 * 5

        limit = 0
        ctx_prof = {}

        if category == 'politician':
            poli = Politician.objects.filter(
                name__icontains=query
            )[page * PAGE_SIZE:page * PAGE_SIZE + PAGE_SIZE]
            ctx_prof = {
                'politician': poli,
                'organization': []
            }
            limit = (
                Politician
                .objects
                .filter(name__icontains=query).count() // PAGE_SIZE
            )

        if category == 'organization':
            org = Organization.objects.filter(
                name__icontains=query
            )[page * PAGE_SIZE:page * PAGE_SIZE + PAGE_SIZE]
            ctx_prof = {
                'organization': org,
                'politician': []
            }
            limit = (
                Organization
                .objects
                .filter(name__icontains=query).count() // PAGE_SIZE
            )

        return {
            'search_results': {
                **ctx_prof,
                'page': {
                    'current': page,
                    'next': page + 1,
                    'previous': page - 1,
                    'limit': limit
                },
                'request': {
                    'query': query,
                    'category': category,
                }
            }
        }

    if request.htmx:
        return render(
            request,
            'search/components/results.html.jinja2',
            create_context()
        )

    return render(
        request,
        'search/search.html.jinja2',
        create_context()
    )
