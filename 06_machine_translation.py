# pip install translate

# Import the Translator class from the translate module
from translate import Translator

# Create a Translator object
# Spanish can be replaced with any other language
translator = Translator(to_lang='es')

# Text to be translated
text = 'Hello, how are you?'

# Perform the translation
translation = translator.translate(text)

# Print the original text
print(f"Original Text: {text}")

# Print the translated text
print(f"Translated Text: {translation}")