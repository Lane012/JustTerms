from TermBuilder.helpers.WordFetcher import WordFetcher
import random

class WordBank():
    
    
    def __init__(self):
        self.WordFetcher =  WordFetcher()
        
    
    def getWords(self, allWords):
        jsonWordObject = self.getWordDictionary()
        
        if(allWords):
            return jsonWordObject  
        
        
        numCount = 0
        keyWords = list(jsonWordObject.keys())
        Words = []
        
        while(numCount < 20):
            keyIndex = random.randint(0, len(keyWords)-1)
            key = keyWords[keyIndex]
            selectedVerb = (keyWords[keyIndex], jsonWordObject[key])
            
            if(key not in dict(Words)):
                Words.append(selectedVerb)
                numCount += 1
        
        return Words
         
          
    def getWordDictionary(self):
        jsonData = self.WordFetcher.getWords()
        jsonWordObject = jsonData["Words"]
        
        return jsonWordObject
        
        
        
        
    
        
    
        
        
    