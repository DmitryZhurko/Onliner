from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from currency.views import core_kurs_dollar
from weather.views import core_weather
# Models
from service.models import Service, Comment, Contractor, Category, Rating, CommentContract

# Forms
from service.forms import CommentForm, ServiceForm, ContractorForm, RatingForm, CommentContractorForm

# Repeat
from service.def_repeat import view_mixin, paginator


def service_home(request):
    page_obj = view_mixin(request, cate_pk=None, queryset=Service.objects.all())

    context = {
        'category': page_obj[0],
        'page_obj': page_obj[1][0],
        'my_filters': page_obj[1][1],
        'kurs_dollar': core_kurs_dollar(request),
        'core_weather': core_weather(request),
    }

    return render(request, 'service/base_service.html', context)


def category_list(request, cate_pk):
    page_obj = view_mixin(request, cate_pk=cate_pk, queryset=Service.objects.filter(category=cate_pk))
    count = Service.objects.filter(category=cate_pk)

    context = {
        'category': page_obj[0],
        'page_obj': page_obj[1][0],
        'my_filters': page_obj[1][1],
        'current_category': cate_pk,
        'count': count
    }

    return render(request, 'service/category_list.html', context)


def service_detail(request, srv_pk):
    service = Service.objects.get(pk=srv_pk)
    comment = Comment.objects.filter(service=srv_pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            cf = comment_form.save(commit=False)
            cf.user = request.user
            cf.service = service
            cf.save()
            return redirect('service:service_detail', srv_pk)
    else:
        comment_form = CommentForm()

    context = {
        'service': service,
        'comment': comment,
        'comment_form': comment_form
    }

    return render(request, 'service/service_detail.html', context)


@login_required
def my_service(request):
    page_obj = view_mixin(request, cate_pk=None, queryset=Service.objects.filter(user=request.user))

    context = {
        'page_obj': page_obj[1][0],
        'my_filters': page_obj[1][1]
    }

    return render(request, 'service/my_service.html', context)


@login_required
def service_delete(request, srv_pk):
    Service.objects.get(pk=srv_pk).delete()

    return redirect('service:my_service')


@login_required
def service_create(request):
    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            sf = service_form.save(commit=False)
            sf.user = request.user
            sf.save()
            return redirect('service:my_service')
    else:
        service_form = ServiceForm()

    context = {
        'service_form': service_form
    }

    return render(request, 'service/service_create.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        service = Service.objects.filter(Q(title__contains=searched) |
                                         Q(description__contains=searched) |
                                         Q(price__contains=searched))

        page_obj = paginator(request, service)

        context = {
            'searched': searched,
            'page_obj': page_obj,
        }

        return render(request, 'service/search.html', context)
