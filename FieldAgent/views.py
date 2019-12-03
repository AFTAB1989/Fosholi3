from django.shortcuts import render


def fa_dashboard(request):
    return render(request, "field-agent-dashboard.html")


def register_farmer(request):
     # form = RegisterForm()
     
    # if request.method == "POST":
    #     form = RegisterForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save(commit=True)  # saves from data in model
    #         messages.success(request, f'New account created successfully !')
    #         return redirect(register)
    #     else:
    #         messages.success(request, f'Could not create new acount. Something went wrong')
    #         return render(request, 'registerChairman.html', {'form': form})
    # return render(request, 'registerChairman.html', {'form': form})
     return render(request, "field-agent-farmer.html")


def survey(request):
    return render(request, "field-agent-survey.html")
