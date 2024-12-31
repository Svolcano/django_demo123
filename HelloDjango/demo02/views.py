from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def index(request):
    template = loader.get_template("demo02/index.html")
    return HttpResponse(template.render(context=None, request=request))