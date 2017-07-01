from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.fields.related import OneToOneField


class Word(models.Model):
    value = models.CharField(max_length=64)
    
class Definition(models.Model):
    value = models.TextField(max_length=500)
    word = OneToOneField(Word, on_delete=models.CASCADE)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    words = models.ForeignKey(Word, on_delete=models.CASCADE, null=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created,  **kwargs):
        
        if(created):
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def setWordList(self, words, definitions):
        self.words = words
        self.definitions = definitions
        self.save()
    
    def getWordList(self):
        return (self.words, self.definitions)
    
 
    

    
    
        
        
    
        