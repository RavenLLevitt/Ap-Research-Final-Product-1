import datetime

#file --VocabWord.py--
class VocabWord:
    word = ''
    currentInterval = 0
    lastRecallDate = 0

    def __init__(self, myWord):
        self.word = myWord
        #not sure if these should be here or above
        self.currentInterval = 0
        self.lastRecallDate = datetime.datetime.now()


    #returns word
    def getword(self):
        return self.word
    
    #precondition: correct is a bool
    def updateInterval(self, correct):
        self.lastRecallDate = datetime.datetime.now()
        if correct:
            #need to unhardcode this also change the 3 if the # of intervals changes
            if self.currentInterval <= 3:
                self.currentInterval += 1
        else:
            self.currentInterval = 0

    def daysSinceLastRecall(self):
        x = datetime.datetime.now()-self.lastRecallDate
        return x.days

