import deepl
translator = deepl.Translator("INSERT KEY")
result = translator.translate_text("hello", target_lang="ES") 
translated_text = result.text
print(translated_text)
print("finished")
