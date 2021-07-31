from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponseRedirect

from service.models import Contractor, CommentContract, Category, Rating

from service.forms import ContractorForm, CommentContractorForm, RatingForm

from service.def_repeat import paginator
from service.contractor.contract_repeat import contract_category


def contractor(request):
    category = contract_category(request)
    contractor = Contractor.objects.all()
    comment_ct = CommentContract.objects.filter(user=request.user)

    page_obj = paginator(request, contractor)

    context = {
        'category': category,
        'page_obj': page_obj,
        'comment_ct': comment_ct
    }

    return render(request, 'service/contractor.html', context)


def contractor_category(request, cate_pk):
    category = contract_category(request)
    contractor = Contractor.objects.filter(work=cate_pk)

    page_obj = paginator(request, contractor)

    context = {'category': category, 'page_obj': page_obj}

    return render(request, 'service/contractor_category.html', context)


def contractor_detail(request, cont_pk):
    contractor = Contractor.objects.get(pk=cont_pk)
    comment_ct = CommentContract.objects.filter(contractor=cont_pk)

    if request.method == 'POST':

        comment_ct_form = CommentContractorForm(request.POST)
        if comment_ct_form.is_valid():
            ccf = comment_ct_form.save(commit=False)
            ccf.user = request.user
            ccf.contractor = contractor
            ccf.save()
            return redirect('service:contractor_detail', cont_pk)

        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rf = rating_form.cleaned_data
            form_user = request.user
            Rating.objects.create(
                contractor=contractor,
                user=form_user,
                rating=rf['rating']
            )
            return redirect('service:contractor_detail', cont_pk=contractor.pk)

    else:
        rating_form = RatingForm()
        comment_ct_form = CommentContractorForm()


    context = {
        'contractor': contractor,
        'rating_form': rating_form,
        'comment_ct': comment_ct,
        'comment_ct_form': comment_ct_form
    }
    return render(request, 'service/contractor_detail.html', context)


@login_required
def contractor_create(request):
    contractor = Contractor.objects.all()

    if request.user.first_name == '':
        return redirect('users:profile')

    elif request.user.last_name == '':
        return redirect('users:profile')

    elif request.user.first_name != '' and request.user.last_name != '':
        return redirect('service:my_contract')

    else:
        if request.method == 'POST':
            contractor_form = ContractorForm(request.POST)
            if contractor_form.is_valid():
                cf = contractor_form.save(commit=False)
                cf.user = request.user
                cf.save()
                return redirect('service:contractor_create')
        else:
            contractor_form = ContractorForm()

    context = {
        'contractor_form': contractor_form
    }

    return render(request, 'service/contractor_create.html', context)


def my_contract(request):
    contractor = Contractor.objects.get(user=request.user)
    comment_ct = CommentContract.objects.filter(user=request.user)

    if request.method == 'POST':

        comment_ct_form = CommentContractorForm(request.POST)
        if comment_ct_form.is_valid():
            ccf = comment_ct_form.save(commit=False)
            ccf.user = request.user
            ccf.contractor = contractor
            ccf.save()
            return redirect('service:my_contract')


        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rf = rating_form.cleaned_data
            form_user = request.user
            Rating.objects.create(
                contractor=contractor,
                user=form_user,
                rating=rf['rating']
            )

            return redirect('service:my_contract')

    else:
        rating_form = RatingForm()
        comment_ct_form = CommentContractorForm()

    context = {'contractor': contractor,
               'comment_ct': comment_ct,
               'comment_ct_form': comment_ct_form,
               'rating_form': rating_form,}

    return render(request, 'service/my_contract.html', context)


def contractor_redact(request):
    contractor = get_object_or_404(Contractor, user=request.user)
    if request.method == 'GET':
        contractor_form = ContractorForm(instance=contractor)
        return render(request, 'service/contractor_redact.html', {'contractor_form': contractor_form})
    else:
        contractor_form = ContractorForm(request.POST, instance=contractor)
        if contractor_form.is_valid():
            cf = contractor_form.save(commit=False)
            cf.save()
            return redirect('service:my_contract')




def contractor_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        contractor = Contractor.objects.filter(Q(user__username__contains=searched) |
                                               Q(user__first_name__contains=searched) |
                                               Q(user__last_name__contains=searched) |
                                               Q(description__contains=searched) |
                                               Q(work__name__contains=searched) |
                                               Q(phone__contains=searched))

        page_obj = paginator(request, contractor)

        context = {
            'searched': searched,
            'page_obj': page_obj
        }

        return render(request, 'service/contractor_search.html', context)
