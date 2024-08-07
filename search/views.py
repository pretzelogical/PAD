from django.shortcuts import render
from common.models import Politician, Organization


def search(request):
    """ Search for either a politician or an organization """
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'politician')
    page = int(request.GET.get('page', '0'))
    PAGE_SIZE = 3 * 3

    def create_context(category, query, page):
        ctx_prof = {}
        if category == 'politician':
            poli = Politician.objects.filter(
                name__icontains=query
            )[page * PAGE_SIZE:page * PAGE_SIZE + PAGE_SIZE]
            org = None
            ctx_prof = {
                'politician': poli,
                'page': {
                    'total': list(
                        range(len(Politician.objects.all()) // PAGE_SIZE)
                    ),
                }
            }

        if category == 'organization':
            org = Organization.objects.filter(
                name__icontains=query
            )[page * PAGE_SIZE:page * PAGE_SIZE + PAGE_SIZE]
            poli = None
            ctx_prof = {
                'organization': org,
                'page': {
                    'total': list(
                        range(len(Organization.objects.all()) // PAGE_SIZE)
                    ),
                }
            }

        if not ctx_prof:
            return {}

        return {
            'search_results': {
                **ctx_prof,
                'request': {
                    'query': query,
                    'category': category,
                }
            }
        }

    print(create_context(category, query, page))

    if request.htmx:
        return render(
            request,
            'search/components/search_results.html.jinja2',
            create_context(category, query, page)
        )

    return render(
        request,
        'search/search.html.jinja2',
        create_context(category, query, page)
    )
