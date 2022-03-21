import VocabWord.py

#just for testing shit
dog = VocabWord("dog")

print(dog.getword())

dog.updateInterval(True)
dog.updateInterval(False)

print(dog.daysSinceLastRecall())
