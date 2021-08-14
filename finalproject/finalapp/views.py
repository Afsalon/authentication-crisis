from django.shortcuts import render
from finalapp import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'finalapp/home.html')

@login_required
def congrats(request):
    return render(request,'finalapp/congrats.html')

@login_required
def signout(request):
    return render(request,'finalapp/signout.html')

def signup(request):
    r = False
    if request.method == 'POST':
        inst_one=forms.UserForm(data=request.POST)
        inst_two=forms.UserProfileForm(data=request.POST)
        if inst_one.is_valid() and inst_two.is_valid():
            user=inst_one.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = inst_two.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            r = True
        else:
            print(inst_one.errors, inst_two.errors)
    else:
        inst_one=forms.UserForm()
        inst_two=forms.UserProfileForm()
    return render(request, 'finalapp/signup.html',{'inst_one':inst_one,'inst_two':inst_two,'r':r})

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('congrats_page'))
            else:
                HttpResponse('Account not active')
        else:
            print('user does not exist')
    else:
        return render(request, 'finalapp/signin.html',{})
