from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session

from DC.models import DC
from UpChairman.models import UpChairman
from UNO.models import UNO
from FieldAgent.models import FieldAgent
from Farmer.models import Farmer
from Miller.models import Miller
from DC import templates

def show(request):
    return render(request, 'projects-no-images.html')


def fHome(request):
    if request.session.has_key('user_id') and request.session.has_key('actor'):
        return render(request, 'farmerHomePage.html')
    else:
        return redirect('/Farmer/login_pg')


def loginFormView(request):
   if request.session.has_key('user_id') and request.session.has_key('actor'):
      user_id = request.session['user_id']
      actor = request.session['actor']
      if actor == "dc":
        return render(request, 'DChome.html', {"user_id" : user_id,"actor":actor})
      elif actor== "farmer":
        return render(request, 'farmerHomePage.html', {"user_id" : user_id,"actor":actor})
      elif actor == "upc":
          return render(request, 'upcHome.html', {"user_id" : user_id,"actor":actor})
      elif actor == "uno":
          return render(request, 'uno-dashboard.html', {"user_id" : user_id,"actor":actor})
      elif actor == "fieldAgent":
          return render(request, 'field-agent-dashboard.html', {"user_id" : user_id,"actor":actor})
   else:
      return render(request, 'login.html')


def login_pg(request):
    if request.method == "POST":
        actor = request.POST.get("actor")
        if actor == "dc":
            dcId = request.POST.get('user_id')
            dcPswrd = request.POST.get('user_password')
            dc = DC.objects.all().filter(dc_id=dcId, dc_password=dcPswrd)

            if dc:
                request.session['user_id'] = dcId
                request.session['actor'] = actor
                return redirect('/DC/')
                # return render(request, 'DChome.html')
            else:
                messages.success(request, f'Invalid DC id or Password...!!')
                render(request,'farmerHomePage.html')

        elif actor == "upc":
            upcId = request.POST.get('user_id')
            upcPswrd = request.POST.get('user_password')
            upc = UpChairman.objects.all().filter(upc_id=upcId, upc_password=upcPswrd)

            if upc:
                request.session['user_id'] = upcId
                request.session['actor'] = actor
                return redirect('/upc/')
            else:
                messages.error(request, 'Invalid Up Chairman id or Password...!!')
                return redirect(login_pg)

        elif actor == "uno":
            unoId = request.POST.get('user_id')
            unoPswrd = request.POST.get('user_password')
            uno = UNO.objects.all().filter(uno_id=unoId, uno_password=unoPswrd)

            if uno:
                request.session['user_id'] = unoId
                request.session['actor'] = actor
                return redirect('/UNO/')
            else:
                messages.error(request, 'Invalid UNO id or Password...!!')
                return redirect(login_pg)

        elif actor == "fieldAgent":
            fieldAgentId = request.POST.get('user_id')
            fieldAgentPswrd = request.POST.get('user_password')
            fieldAgent = FieldAgent.objects.all().filter(fa_id=fieldAgentId, fa_password=fieldAgentPswrd)

            if fieldAgent:
                request.session['user_id'] = fieldAgentId
                request.session['actor'] = actor
                return redirect('/FieldAgent/')
            else:
                messages.error(request, 'Invalid Field Agent id or Password...!!')
                return redirect(login_pg)

        elif actor == "farmer":
            farmerId = request.POST.get('user_id')
            farmerPswrd = request.POST.get('user_password')
            farmer = Farmer.objects.all().filter(f_id=farmerId, f_password=farmerPswrd)

            if farmer:
                request.session['user_id'] = dcId
                request.session['actor'] = actor
                return redirect('/Farmer/')
            else:
                messages.error(request, 'Invalid Farmer id or Password...!!')
                return redirect(login_pg)

        elif actor == "miller":
            millerId = request.POST.get('user_id')
            millerPswrd = request.POST.get('user_password')
            miller = Miller.objects.all().filter(m_id=millerId, m_password=millerPswrd)

            if miller:
                return redirect('/Miller/')
            else:
                messages.error(request, 'Invalid miller id or Password...!!')
                return redirect(login_pg)

    return render(request, 'login.html')
