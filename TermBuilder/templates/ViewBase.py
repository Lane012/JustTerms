from django.template.exceptions import TemplateDoesNotExist
from TermBuilder.helpers.WordBank import WordBank
import random


# ViewHelpers job is to prevent repetitive operations (Code repeat) such as fetching resources from database
# any forseeable repetition will be encapsulated inside the ViewHelper class

class ProfileHelper():
    profile = ''
    
    def __init__(self, profile):
        self.profile = profile
    
    def getResources(self): 
        wordList = self.getProfileWordList()
        resources = {"words": wordList}
        
        return resources
    
    def getMasteredWords(self):
        masteredWords = self.getMasteredWordsInProfileList()
        return masteredWords
    
    def getMasteredWordCount(self):
        
        masteredCount = self.getMasteredAmount()
        return masteredCount
    
    def getLastTestScore(self):
        testScore = self.profile.lastTestScore
        return testScore
    
    def getTestScore(self):
        testScore = self.profile.currentTestScore
        return testScore
    
    def getTotalTestTaken(self):
        totalTestTaken = self.profile.totalTestTaken
        return totalTestTaken
    
    def getTotalPassedTest(self):
        totalPassedTest = self.profile.totalTestPassed
        return totalPassedTest
        
        
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
    
    def getTotalWordCount(self):
        
        wordTotal = self.getTotalNumOfWords()
        return wordTotal
        
    
    
    
     
class ExamHelper():
    profile = ''
    profileHelper = ''
    wordList = ''
    answers = []
    questions = []
    
    def __init__(self, profile):
        self.profile = profile
        
    
    
    def createTest(self):
        profileHelper = ProfileHelper(self.profile)
        
        self.wordList = profileHelper.getProfileWordList()
        
        ExamData = self.getTestData()
        
        return ExamData
        
    
    def getTestData(self):
        examData = {}
        indexesUsed = []
        
        while(len(indexesUsed) < 20):
            wordIndex = random.randint(0, 19)
            
            if wordIndex not in indexesUsed:
                
                indexesUsed.append(wordIndex)
                currentWord = self.wordList[wordIndex]
                
                self.answers.append(currentWord.value)
                currentDef = currentWord.definition.value
                
                self.questions.append(currentDef)
                examData[currentDef] = self.getOptions(currentWord)
                
        return examData
    
        
    def getAnswerKey(self):
        return self.answers
    
    def getQuestions(self):
        return self.questions
    
    def getOptions(self, currentWord):
        counter = 1
        options = []   
        pluginFlag = random.randint(1, 4) # this determines where the correct answer appears in options 
             
        while(counter < 5):
            
            if(counter == pluginFlag):
                options.append(currentWord.value)
                counter += 1
            
            else: 
                incorrectWord = self.wordList[random.randint(0, 19)]
                
                if(incorrectWord.value not in options and incorrectWord.value != currentWord.value):
                    options.append(incorrectWord.value)
                    counter += 1
        
        return options
            
            
            
            
            
                
                
                
                        
                    
                
            
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    