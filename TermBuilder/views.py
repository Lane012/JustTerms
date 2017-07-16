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
from django.conf.global_settings import LOGIN_REDIRECT_URL



@login_required
def home_page(request):
	profile = request.user.profile
	numOfWords = profile.getWordCount()
	numberedMastered = profile.masteredwords.words.count()  #refractor this line (violates law of demeter)
	
	
	
	context = {}
	
	template = loader.get_template('home_page.html')
	mastered_words = get_mastered_words_in_current_list(profile)
	
	if numOfWords > 0:
		context = {"words": profile.getWordList(), "mastered_Words": mastered_words, "masteredWordCount": numberedMastered}
		
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
	assert(user.is_authenticated(), "User is not logged in")
	
	userProfile = user.profile
	words = get_every_word()
	
	if userProfile.getWordCount() > 0:
		userProfile.clearWordList()
	for term, meaning in wordList:
			for word in words:
				if(term.upper() == word.value):
					userProfile.addWord(word)
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

def get_mastered_words_in_current_list(profile):
	green_words = []
	
	words = profile.getWordList()
	for word in words:
		if(word in profile.masteredwords.words.all()):
			green_words.append(word)
	
	return green_words
	
	




		
	
	
	
	