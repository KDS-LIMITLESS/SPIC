from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UpdateFormFields, UpdateProfile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')  #ERROR still here come back!!!!
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html',{'form': form, 'title':'Register'})
    
@login_required
def profile(request):
    if request.method == 'POST':
        FormField = UpdateFormFields(request.POST, instance=request.user)
        Update_Profile = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)

        if FormField.is_valid() and Update_Profile.is_valid():
            FormField.save()
            Update_Profile.save()

            messages.success(request, f'Your Account has been Updated!')  
            return redirect('profile')
    else:
        FormField = UpdateFormFields(instance=request.user)
        Update_Profile = UpdateProfile(instance=request.user.profile)

    context = {

        'FormField' : FormField,
        'Update_Profile': Update_Profile
    }
    return render(request, 'user/profile.html', context)