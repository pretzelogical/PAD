from django.shortcuts import render
from common.models import Politician, Organization

# Create your views here.


def profile(request, **kwargs):
    category = kwargs.get('category', None)
    target_id = kwargs.get('target_id', None)

    if category == 'politician':
        context = {
            'profile': Politician.objects.get(id=target_id),
        }
        return render(request, 'profiles/profile.html.jinja2', context)
    if category == 'organization':
        context = {
            'profile': Organization.objects.get(id=target_id),
        }
        return render(request, 'profiles/profile.html.jinja2', context)

    return render(request, 'profiles/profile.html.jinja2')
