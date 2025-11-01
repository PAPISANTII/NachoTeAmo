from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

def register(request):
    return render(request, "users/register.html")

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            messages.success(request, "Usuario registrado correctamente :)")
            return redirect('macarrones:home')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("macarrones:home")
    else:       
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})
    
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "Has cerrado sesion correctamente. :( ")
        return redirect('macarrones:home')
    else:
        return redirect('macarrones:home')