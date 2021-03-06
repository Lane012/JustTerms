from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.fields.related import OneToOneField




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    currentTestScore = models.IntegerField(default=0)
    lastTestScore = models.IntegerField(default=0)
    totalTestTaken = models.IntegerField(default=0)
    totalTestPassed = models.IntegerField(default=0)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created,  **kwargs):
        
        if(created):
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def addWord(self, word):
        self.word_set.add(word)
        self.save()
    
    def getWordCount(self):
        return self.word_set.count()
    
    def getWordList(self):
        return self.word_set.all()
    
    def clearWordList(self):
        self.word_set.clear()
        
    def getTotalTestTaken(self):
        return self.totalTestTaken
    
    def getTotalTestPassed(self):
        return self.totalTestPassed
        
class Word(models.Model):
    value = models.CharField(max_length=64, null=True)
    profile = models.ManyToManyField(Profile)
    
    
class Definition(models.Model):
    value = models.TextField(max_length=500, null=True)
    word = OneToOneField(Word, on_delete=models.CASCADE, null=True, unique=True)
    
    
class MasteredWords(models.Model):
    profile = OneToOneField(Profile, on_delete=models.CASCADE, unique=True)
    words = models.ManyToManyField(Word)
    
    

    

    
 
    

    
    
        
        
    
        