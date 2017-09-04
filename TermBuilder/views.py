from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from TermBuilder.helpers.WordBank import WordBank
from TermBuilder.helpers.TemplateLoader import TemplateLoader
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from TermBuilder.models import Word, Definition
from django.contrib.auth import login
from django.conf.global_settings import LOGIN_REDIRECT_URL
from TermBuilder.templates.ViewBase import ProfileHelper, WordHelper, ExamHelper


@login_required
def home_page(request):
	profile = request.user.profile
	if request.method == "GET":
		profileHelper = ProfileHelper(profile)
		template = TemplateLoader().loadTemplate("home_page.html")
		
		if(type(template) == HttpResponseRedirect):
			return template

		numOfWords = profileHelper.getWordCount()
		context = {}
		
		if numOfWords > 0:
			context = profileHelper.getResources()
			context["mastered_words"] = profileHelper.getMasteredWords()
			context["masteredWordCount"] = profileHelper.getMasteredWordCount()
			context["test_score"] = profileHelper.getTestScore()
			context["last_test_score"] = profileHelper.getLastTestScore()
			context["wordTotal"] = WordHelper().getTotalWordCount()
			context["totalTestTaken"] = profileHelper.getTotalTestTaken()
			context["totalPassedTest"] = profileHelper.getTotalPassedTest()
		
			
		return TemplateResponse(request, template, context)


@login_required
def study_page(request):
	profile = request.user.profile
	if request.method == "GET":
		profileHelper = ProfileHelper(profile)
		template = TemplateLoader().loadTemplate("study.html")
		
		if(type(template) == HttpResponseRedirect):
			return template
		
		context = profileHelper.getResources()
		
		response = TemplateResponse(request, template, context)
		
		return response
	
@login_required
def test_page(request):
	profile = request.user.profile
	
	if request.method == "GET":
		examHelper = ExamHelper(profile)
		template = TemplateLoader().loadTemplate("test.html")
		testData = examHelper.createTest()
		context = {"TestData": testData}
		context["answers"] = examHelper.getAnswerKey()
		context["questions"] = examHelper.getQuestions()
		
		return TemplateResponse(request, template, context)
		
	
	
	
	
	
	
	
			
   	 	     		

def create_user_word_list(request):
	wordList = []
	user = request.user
	user.profile.lastTestScore = user.profile.currentTestScore
	user.profile.currentTestScore = 0

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


def test_score_update(request):
		
	user = request.user
	profile = user.profile
	if(user.is_authenticated()):
		testScore = int(request.body.decode("utf-8"))
		
		if(testScore >= 0 and testScore <= 20):
			profile.currentTestScore = (testScore/20 * 100)
			
			if(testScore >= 14):
				profile.totalTestPassed += 1
			
			profile.totalTestTaken += 1
			profile.save()
			
	return HttpResponse("")



	
	

	
	




		
	
	
	
	