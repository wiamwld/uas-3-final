from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import blog
# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog(request):
    context = {
        'Form': ContactForm,
    }
    return render(request, 'blog.html',context)


def Send_contact(request):
    if request.POST:
        Form = ContactForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
        return redirect('/contact')
    return redirect('/contact')
