from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse


def home_page(request):
	template = loader.get_template('home_page.html')
	return TemplateResponse(request, template, {})

