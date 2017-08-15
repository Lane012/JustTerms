from django.template.exceptions import TemplateDoesNotExist
from TermBuilder.helpers.WordBank import WordBank


# ViewHelpers job is to prevent repetitive operations (Code repeat) such as fetching resources from database
# any forseeable repetition will be encapsulated inside the ViewHelper class

class ProfileHelper():
    profile = ''
    
    def __init__(self, profile):
        self.profile = profile
    
    def getResources(self,masteredNeeded=False, masteredCountNeeded=False): 
        wordList = self.getProfileWordList()
        
        resources = {"words": wordList}
        
        if(masteredNeeded):
            masteredWords = self.getMasteredWordsInProfileList()
            resources["mastered_Words"] = masteredWords
        
        if(masteredCountNeeded):
            masteredCount = self.getMasteredAmount()
            resources["masteredWordCount"] = masteredCount
        
        return resources
            
    
    def getWordCount(self):
        numOfWords = self.profile.getWordCount()
        return numOfWords
    
    
    def getProfileWordList(self):
       wordList = self.profile.getWordList()
       return wordList
   
   
    def getMasteredAmount(self):
        numberedMastered = self.profile.masteredwords.words.count()  
        return numberedMastered
    
    
    def getMasteredWordsInProfileList(self):
        green_words = []
        
        words = self.profile.getWordList()
        for word in words:
            if(word in self.profile.masteredwords.words.all()):
                green_words.append(word)
        
        return green_words
    
    
    

class WordHelper():
    
    def getTotalNumOfWords(self):
        words = WordBank().getWords(True)
        
        wordCount = len(words.keys())
        
        return wordCount
    
    def addTotalWordCount(self, context):
        
        context["wordTotal"] = self.getTotalNumOfWords()
        
    
    
    
    