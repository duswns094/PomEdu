from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    if request.user.is_anonymous:
        return redirect("accounts:login")
    return render(request, "homeapp/index.html")