from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('isicwebdatabase:index-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"
    model = User
    
