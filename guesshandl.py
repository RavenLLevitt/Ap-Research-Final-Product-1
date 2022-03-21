

from googletrans import Translator

def translateJ(self, preTrans):
    translator = Translator()
    posTrans = translator.translate(preTrans, dest = "ja")
    return posTrans

