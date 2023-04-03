from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CheckinCheckout, CustomUser
from django.shortcuts import redirect
from django.utils import timezone

@login_required
def chkout(request):
    userCheckin = CheckinCheckout.objects.filter(employee=request.user).order_by('-id')[0]
    # userCheckin = CheckinCheckout(employee=request.user)
    # import pdb;pdb.set_trace()
    # userCheckin.save()
    userCheckin.checkout_time = timezone.now()
    userCheckin.save()

    userCheckin.employee.is_working = False
    userCheckin.employee.save()
    return redirect('home')

@login_required
def chkin(request):
    userCheckin = CheckinCheckout(employee=request.user)
    # import pdb;pdb.set_trace()
    userCheckin.employee = request.user
    userCheckin.save()

    userCheckin.employee.is_working = True
    userCheckin.employee.save()
    return redirect('home')