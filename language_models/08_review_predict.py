# pip install scikit-learn

# import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# sample reviews and their corresponding labels
reviews = [
    'This movie was fantastic! A must-watch.',
    'I didn\'t enjoy this movie at all.',
    'Amazing storyline and great acting!',
    'The plot was dull and predictable.',
    'Loved the cinematography! Highly recommended.'
]

labels = [
    'positive',
    'negative', 
    'positive', 
    'negative', 
    'positive'
]

# create a CountVectorizer object
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

# split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

# create a Multinomial Naive Bayes classifier
model = MultinomialNB()
model.fit(x_train, y_train)

# make predictions
y_pred = model.predict(x_test)

# calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# print the accuracy of the model
print(f"Accuracy: {accuracy}")
print()

# check if the accuracy is greater than 0.8
if accuracy > 0.8:
  print('Good vibes. Book the ticket!')
else:
  print('Needs more work!')