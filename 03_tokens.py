# Generate tokens from a sample text using NLTK
import nltk

# Download the Punkt tokenizer
nltk.download('punkt_tab')

# Tokenize the sample text
from nltk.tokenize import word_tokenize

sample_text = 'I am learning Generative AI'

# Convert the text to lowercase
tokens = nltk.word_tokenize(sample_text.lower())

print('Tokens:', tokens)