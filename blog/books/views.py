from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from .models import Book
from books.forms import ContactForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages



class BookListView(ListView):
    model = Book
    template_name = 'hello.html'
    context_object_name = 'books'
    
class MyView(View):
    def get(self, request):
        return HttpResponse('Welcome to Django from Class!')    

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    
    
# python generator, threading, asyn, syn, DRY, WAIT, KISS, 
# New function before __init__
# Q, F, Sum, Count, Avg, Prefetch(for many to many), select_related(for one to many)
# Https status code
# Html template tags

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        # Custom behavior (optional)
        return super().form_valid(form)
    
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            messages.success(request, 'Registration successful.')
            return redirect('books/list/')  # Redirect to the homepage or any other page
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})
    