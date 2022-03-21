import deepl
translator = deepl.Translator("b92d0f2a-2c86-3f15-b9e9-4f44fc65fd02:fx")
result = translator.translate_text("hello", target_lang="ES") 
translated_text = result.text
print(translated_text)
print("finished")