from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from TermBuilder.helpers.WordBank import WordBank
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home_page(request):
	template = loader.get_template('home_page.html')
	return TemplateResponse(request, template, {})


def create_user_word_list(request):
	wordList = []
	if(request.user.is_authenticated()):
		wordList = WordBank().getWords()
		request.user.profile.setWordList(wordList)
		
	jsonWord = {"Words": []}
	
	for key, value in wordList:
		dict = {}
		dict[key] = value
		jsonWord["Words"].append(dict)
	
	
	return HttpResponse(json.dumps(jsonWord))