from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

# VIEW
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Login MIXIN
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# from account.mixins import LogoutRequiredMixin

# forms
from django.contrib.auth.forms import AuthenticationForm

# models
from django.contrib.auth.models import User
from todoapp.models import todo

# message
from django.contrib import messages

import uuid
from django.db.models import Q

# Create your views here.

@login_required
def home(request):
    current_user = request.user
    all_task = todo.objects.filter(user=current_user)
    if request.method == "POST":
        name = request.POST.get('todo_name')
        new_todo = todo(user=request.user, tode_description=name)
        new_todo.save()
        messages.success(request, 'New task created!')
        return redirect('home')

    context = {
        'all_task': all_task
    }
    return render(request, 'todoapp/todo.html', context)

@login_required
def upadate_task(request, id):
    task = todo.objects.get(user=request.user, id=id)
    task.status = True
    task.save()
    messages.success(request, 'task updated')
    return redirect(home)

@login_required
def delete_task(request, id):
    task = todo.objects.get(user=request.user, id=id)
    task.delete()
    messages.success(request, 'task Deleted!!')
    return redirect(home)


def register(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')

        if password == password2:
            if User.objects.filter(username=name).exists():
                messages.error(request, 'User already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                obj = User.objects.create_user(
                    username=name, email=email, password=password)
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.error(request, 'password doesnt match')
            return redirect('register')
    return render(request, 'todoapp/register.html')


def login_page(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=name).exists():
            messages.error(request, 'Please input your valid Username')
            return redirect('login')

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Password incorrect!')
            return redirect('login')
    return render(request, 'todoapp/login.html')


@login_required
def logout_page(request):
    logout(request)
    messages.error(request, 'Logout successfull, please login here!')
    return redirect('login')
