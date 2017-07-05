from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.fields.related import OneToOneField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
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
    
    def getWordList(self):
        return self.word_set

class Word(models.Model):
    value = models.CharField(max_length=64, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    
    
class Definition(models.Model):
    value = models.TextField(max_length=500, null=True)
    word = OneToOneField(Word, on_delete=models.CASCADE, null=True)
    

    
 
    

    
    
        
        
    
        