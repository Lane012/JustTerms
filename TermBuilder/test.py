from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from TermBuilder import models
from TermBuilder.helpers.WordBank import WordBank
from TermBuilder.models import Word, Definition
from TermBuilder.views import create_words_and_definitons_for_user, get_every_word
from django.test.testcases import _AssertTemplateUsedContext

class TestHomePage(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testUser")
        self.user.set_password("12345")
        self.user.save()
        self.client = Client()
        self.client.login(username="testUser", password="12345")
        
        
    def test_home_page_template_extends_base(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home_page.html")
        
    def create_words_and_definitions(self, wordList):
        for term, meaning in wordList:
            word = Word()
            word.value = term.upper()
            word.save()
            definition = Definition()
            definition.value = meaning
            definition.word = word
            definition.save()
            
            
    def test_create_words_and_definitions_for_user_creates_twenty_words(self):
        wordBank = WordBank()
        wordList = wordBank.getWords(False)
        self.create_words_and_definitions(wordList)
        create_words_and_definitons_for_user(self.user, wordList)
        
        self.assertEqual(20, self.user.profile.word_set.count())
        
        
        
        
    
    
        

class TestUserProfile(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username="testUser")
        self.user.set_password("12345")
        self.user.save()
        
    
    def test_user_creates_profile_when_created(self):
        profile = type(self.user.profile)
        self.assertEqual(models.Profile, profile)
    
        
    
    
        

        
    
    
    
    
