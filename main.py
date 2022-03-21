
from transformers import pipeline
from VocabWord import VocabWord
import torch
import torch.nn.functional as F
import DeckHandler


model_name = "gagan3012/k2t-new"

text2text_generator = pipeline("text2text-generation", model=model_name)

#declerations, oscar idc what you think this makes so much mroe sense i'm not doing it your way i simply do not care
nouns = DeckHandler()
verbs = DeckHandler()
adjectives = DeckHandler()

#temp words that are added just for testing, remove later
nouns.addWord("monkey")
verbs.addWord("attack")
adjectives.addWords("cute")


#creates and outputs a new sentance with the key2text model
#change to correct version of keytotext in comment above
def Sgen(Cnoun, Cverb):
    return text2text_generator(Cnoun,Cverb)


