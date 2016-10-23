from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.views.generic import TemplateView

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# class AboutView(TemplateView):
#     template_name = "index.html"


from django.template import loader

from .models import Question


def index(request):
    template = loader.get_template('todo/index.html')
    return HttpResponse('todo/index.html')
