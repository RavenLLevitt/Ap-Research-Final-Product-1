from tkinter import Place
import streamlit as st
import PlaceWhereYouDoReviews

def app():

    #fix english
    st.title("Add a card to your deck")

    #rewrite all of your words cause they suck rn but english is hard and python is cool so just keep going :)
    #also maybe add more choices like adverb or dont idc also maybe do something wierhd with adjectives
    #also also somthing about this order feels gross, fix it
    VocabWordType = st.selectbox("Choose a word type", ["Noun","Adjective","Verb"])

    ActualVocabWord = st.text_input("New Word")

    #need to add somthing that goes, when button clicked add word to siwtch statement adj, noun, verb place

    st.button("submit", on_click=addAWord(ActualVocabWord, VocabWordType))

#fix the palcewhere back to main and recentiarlize please if oyu can
def addAWord(theWordWeAreAdding, wordType):
    match wordType:
        case "Noun":
            PlaceWhereYouDoReviews.nouns.addWord(theWordWeAreAdding)
        case "Adjective":
            PlaceWhereYouDoReviews.adjectives.addWord(theWordWeAreAdding)
        case "Verb":
            PlaceWhereYouDoReviews.verbs.addWord(theWordWeAreAdding)
