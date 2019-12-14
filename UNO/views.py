from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView

from UNO.forms import RegisterForm
from FieldAgent import models
from Farmer.models import Farmer
from .models import UNO


def show(request):
    return render(request, 'uno-agent.html')

def unoHome(request):
    if request.session.has_key('user_id') and request.session.has_key('actor'):
        totalFarmers = Farmer.objects.raw('Select * from Farmer_Farmer') 
        return render(request, 'uno-dashboard.html',{'tf':totalFarmers})
    else:
        return redirect('/Farmer/login_pg')

# UPC registering UNO page
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)  # saves from data in model
            messages.success(request, f'New Field Agent added successfully !')
            return redirect(register)
        else:
            messages.success(request, f'Could not create new account. Something went wrong')
            return render(request, 'registerFA.html', {'form': form})
    return render(request, 'registerFA.html', {'form': form})


#profile page 
def logout(request):
   try:
      del request.session['user_id'] 
      del request.session['actor']
   except:
      pass
   return render(request,'login.html')

def editProfile(request):
    user_id = user_id = request.session['user_id']

    data = get_object_or_404(UNO, pk = user_id)

    if request.method == "POST":
        form = LaptopForm(request.POST,instance =data)
        if form.is_valid():
            form.save()
            return redirect('')
    else: 
        form = laptopForm(instance=item)
        return(request,'edit-profile.html',{'form':form})


def profile(request):
    user_id = request.session['user_id']
    profileData =  UNO.objects.all().filter(uno_id=user_id)
    if profileData:
        return render(request, 'profile.html', {'user_data': profileData})
    else: 
        return HttpResponse('Could not retrive profile information')

def unoUpdate(UpdateView):
    model = UNO
    fields = ['uno_name','uno_phone','uno_address','uno_email','uno_nid_no']
    template_name_suffix = '_update_form'




