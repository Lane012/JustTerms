from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from TermBuilder.helpers.WordBank import WordBank
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from TermBuilder.models import Word, Definition
from django.contrib.auth import login



@login_required(redirect_field_name="/")
def home_page(request):
	profile = request.user.profile
	numOfWords = profile.word_set.count()
	
	context = {}
	
	template = loader.get_template('home_page.html')
	
	if numOfWords > 0:
		context = {"words": profile.word_set.all()}
		
	return TemplateResponse(request, template, context)


def create_user_word_list(request):
	wordList = []
	user = request.user
	if(user.is_authenticated()):
		wordList = WordBank().getWords(False)
		create_words_and_definitons_for_user(user, wordList)
	

	jsonWord = {"Words": []}
	
	for key, value in wordList:
		dict = {}
		dict[key] = value
		jsonWord["Words"].append(dict)
	
	
	return HttpResponse(json.dumps(jsonWord))



def create_words_and_definitons_for_user(user, wordList):
	userProfile = user.profile
	words = get_every_word()
	
	if userProfile.word_set.count() > 0:
		userProfile.word_set.clear()
	
	for term, meaning in wordList:
			for word in words:
				if(term.upper() == word.value):
					userProfile.word_set.add(word)
					break;
		


def format_words_and_definitions_to_strings(wordList):
	words = ""
	definitions = ''
	for word, definition in wordList:
		delimiter = '; '
		words += word + delimiter
		definitions += definition + delimiter
	
	return (words, definitions)


def get_every_word():
	words = Word.objects.all()
	return words




		
	
	
	
	