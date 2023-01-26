from transformers import pipeline
import streamlit as st
from VocabWord import VocabWord
import torch
import torch.nn.functional as F
from DeckHandler import DeckHandler
import deepl

#text gen model decelarations
model_name = "gagan3012/k2t-new"

text2text_generator = pipeline("text2text-generation", model=model_name)

#translator decleration
translator = deepl.Translator("INSERT KEY")

#deck type declerations, maybe add additional word types?
nouns = DeckHandler()
verbs = DeckHandler()
adjectives = DeckHandler()

#temp words that are added just for testing, remove later



#creates and outputs a new sentance with the key2text model
#change to correct version of keytotext in comment above
#needs to be changed so that it can also get in adjectives somtimes, maybe use a switch + randomizer to change between adjective and verb, or just use both and check which it actually uses
def Sgen(Cnoun, Cverb, Cadj):
    noIdeas = text2text_generator(Cnoun, Cverb, Cadj)
    st.text(Cnoun +""+ Cverb + ""+ Cadj)
    return noIdeas

def app():
    ### need to figure out how to make the text go inside of the box maybe
    TheSentanceToGuess = str(goGetterDone())
    TheSentanceToGuess = TheSentanceToGuess[21:len(TheSentanceToGuess)-3]
    result = translator.translate_text(TheSentanceToGuess, target_lang="JA") 
    translated_text = result.text   
    st.text(translated_text)
    st.text(TheSentanceToGuess)
    testing = st.text_input("Guess:")

    st.button("Next word (temp)")
# bad name fix, generates the next sentacne
#need to do testing on what is best to input for program
def goGetterDone():
    return Sgen(nouns.getNextReview(), verbs.getNextReview(), adjectives.getNextReview())

