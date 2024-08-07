from django.shortcuts import render
from common.models import Politician, Organization

# Create your views here.


def profile(request, **kwargs):
    category = kwargs.get('category', None)
    target_id = kwargs.get('target_id', None)

    if category == 'politician':
        poli = Politician.objects.get(id=target_id)
        poli.views += 1
        poli.save()
        context = {
            'profile': poli,
        }
        return render(request, 'profiles/profile.html.jinja2', context)
    if category == 'organization':
        org = Organization.objects.get(id=target_id)
        org.views += 1
        org.save()
        context = {
            'profile': org
        }
        return render(request, 'profiles/profile.html.jinja2', context)

    return render(request, 'profiles/profile.html.jinja2')
