import os
import json
class WordFetcher():
    
    def getWords(self):
        self.changeDirectoryToReadWordFile()
        
        with open("words.json", 'r') as f:
            words = json.load(f)
            return words
        
        
    def changeDirectoryToReadWordFile(self):
        if("TermBuilder/static" not in os.getcwd()):
            os.chdir("TermBuilder/static")
        


        
        
