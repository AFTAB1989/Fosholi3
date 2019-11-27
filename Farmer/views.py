from pyexpat.errors import messages

from django.http import HttpResponse
from django.shortcuts import render, redirect
from DC.models import DC
from UpChairman.models import UpChairman
from UNO.models import UNO
from FieldAgent.models import FieldAgent
from Farmer.models import Farmer
from Miller.models import Miller


def show(request):
    return render(request, 'projects-no-images.html')


def login_pg(request):
    if request.method == "POST":
        actor = request.POST.get("actor")
        if actor == "dc":
            dcId = request.POST.get('user_id')
            dcPswrd = request.POST.get('user_password')
            dc = DC.objects.all().filter(dc_id=dcId, dc_password=dcPswrd)

            if dc:
                return redirect('DC/show')
            else:
                messages.error(request, 'Invalid DC id or Password...!!')
                return redirect(login_pg)

            # elif actor=="upc":
            #    upcId = request.POST.get('user_id')
            #    upcPswrd = request.POST.get('user_password')
            #    dc = DC.objects.all().filter(dc_id=dcId, dc_Password=dcPswrd)
            #
            #    if dc:
            #        return redirect('DC/show')
            #    else:
            #        messages.info(request, 'Invalid DC id or Password...!!')
            #        return redirect(login_pg)
    return render(request, 'login.html')
