from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from TermBuilder import models
from TermBuilder.helpers.WordBank import WordBank

class TestHomePage(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_page_resolves_(self):
        response = self.client.get('/')
        
     
    def test_home_page_template_extends_base(self):
        response = self.client.get('/')
        self.assertIn("HomePage", response.content.decode())
    
        

class TestUserProfile(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username="Lane", password="1234")
        
    
    def test_user_creates_profile_when_created(self):
        profile = type(self.user.profile)
        self.assertEqual(models.Profile, profile)
    
    
    
    
    def test_user_accepts_word_list(self):
        wordList = WordBank().getWords()
        userProfile = self.user.profile
        userProfile.setWordList(wordList)
        self.assertEquals(wordList, userProfile.getWordList())
        

        
    
    
    
    
