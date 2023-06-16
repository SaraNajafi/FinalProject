from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from accounts.forms import RegistrationForm
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # form = AuthenticationForm(request=request, data= request.POST)
            # if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                user = User.objects.filter(Q(username=username) | Q(email=username)).first()
                if user is not None:
                    user = authenticate(request, 
                                    username=user.username, 
                                    password=password)
                    if user is not None:
                    # User is found based on email
                        user = authenticate(request, 
                                    username=user.username, 
                                    password=password)
                        if user is not None:
                            login(request, user)
                            return redirect('/')
        # form = AuthenticationForm()
        # context={'form': form}
        return render(request, 'accounts/login.html')
    else:
        return redirect('/')



@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


# def signup_view(request):
#     if not request.user.is_authenticated:
#         if request.method=='POST':
#             form = UserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')
#             else:
#                  messages.add_message(request, messages.ERROR, f'You didnt sign up. Please try again.'+ messages.error)
#         form = UserCreationForm()
#         context={'form': form}
#         return render(request, 'accounts/signup.html', context)
#     else:
#         return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                 messages.add_message(request, messages.ERROR, f'You didnt sign up. Please try again.')
        form = RegistrationForm()
        context={'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')