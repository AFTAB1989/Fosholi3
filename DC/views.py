from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from DC.forms import registerForm
from django.contrib import messages

# DC index page
def show(request):
    if request.session.has_key('user_id') and request.session.has_key('actor'):
        return render(request, 'DChome.html',{'user_id':user_id,'actor':actor})
    else:
        return redirect('/Farmer/login_pg')



# dc login page
def login_pg(request):
    return render(request, 'upcReg.html')


# dc chairman register page
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True) #saves from data in model
            messages.success(request, f'New account created successfully !')
            return redirect(register)
        else:
                messages.success(request, f'Could not create new acount. Something went wrong')
                return render(request, 'registerChairman.html',{'form':form})

    return render(request, 'registerChairman.html', {'form': form})
