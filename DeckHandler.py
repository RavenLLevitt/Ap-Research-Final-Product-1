import random

from VocabWord import VocabWord

class DeckHandler:
    currentReviews = []
    pendingReviews = []
    intervalTimes = [1,5,10,20]

    #init, could potentially add the ability to create diffrent inverval times for each type but idk if there is any reason for that
    def __init__(self):
        self.currentReviews = []
        #again, idk if i need these but they;re here just incase
        self.pendingReviews = []
        self.intervalTimes = [1,5,10,20]

    #adds a new word to the list of words
    def addWord(self, newWord):
        theWordsWeCreate = VocabWord(newWord)
        self.currentReviews.append(theWordsWeCreate)
    
    #takes in the index of a word and moves it from the current reviews to pending reviews, additionally now updates the interval for convience
    def reviewed(self, currentIndex):
        self.currentReviews[currentIndex].updateInterval(True)
        self.pendingReviews.append(self.currentReviews[currentIndex])
        self.currentReviews.pop(currentIndex)
    #maybe chain getNextReview here later, kinda depends how you want to write it

    #moves all things that need to be reviewed from pending to current reviews
    #high chance of not working correctly, likly needs to be tested then updated
    def recentReviewsCheck(self):
        for i in self.pendingReviews:
            if i.daysSinceLastRecall > self.intervalTimes[i.currentInterval]:
                self.currentReviews.append(i)
                self.pendingReviews.remove(i)

    #gets a random review from the list of current reviews
    #small posiblity it will be impossible to hit the last elemtn in list, make sure this is not the case
    def getNextReview(self):
        r = random.randrange(0, len(self.currentReviews))
        return self.currentReviews[r].word
        
