from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, template_name="demo01/index.html", context=None)