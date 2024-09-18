import nltk
from nltk import word_tokenize

# Generate n-grams from a sample text using NLTK
from nltk.util import ngrams

sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text)

# Unigram (1-gram)
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

print()

# Bigram (2-gram)
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

print()

# Trigram (3-gram)
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)