from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CustomUser, Post
from .forms import ProfileForm, CreatePostForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ['email',]

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
    
class LoginView(LoginView):
    template_name = 'login.html'

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

class ListView(ListView):
    model = Post
    template_name = 'post_list.html'

class DetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class CreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = CreatePostForm
    success_url = '/list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'

class DeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'