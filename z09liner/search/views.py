from django.db.models import Q
from django.shortcuts import render
from service.models import Service
from forum.models import Topic, Post


def search(request):
    zapros = request.GET.get('zapros')
    service_search = Service.objects.filter(
                                 Q(title__contains=zapros) |
                                 Q(description__contains=zapros)
                                 )
    forum_search = Topic.objects.filter(Q(title__contains=zapros))
    context = {
        'zapros': zapros, 'service_search': service_search,
        'forum_search': forum_search,
        }
    return render(request, 'search/search.html', context)