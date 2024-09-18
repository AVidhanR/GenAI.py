# pip install textblob

# Import the necessary libraries
from textblob import TextBlob

# Text to be checked
text = 'I love progamming and machine learnig.'

# Create a TextBlob object
blob = TextBlob(text)

# Perform the spell check
corrected_text = blob.correct()

# Print the original text
print(f"Original Text: {text}")

# Print the corrected text
print(f"Corrected Text: {corrected_text}")