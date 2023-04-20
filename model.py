
import pandas as pd
import streamlit as st
import numpy as np

dataset = pd.read_csv('spam.csv', encoding="ISO-8859-1")

dataset.columns

dataset.drop({'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'}, axis=1, inplace=True)
# st.subheader('Using Following data to train')
# st.dataframe(dataset.head(20))
dataset.head

dataset['v1']=dataset['v1'].map({'ham':0, 'spam':1})

dataset.head

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

cv=CountVectorizer()

X=dataset['v2']
y=dataset['v1']

X=cv.fit_transform(X)

X

x_train, x_test,y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=42)

from sklearn.naive_bayes import MultinomialNB

model=MultinomialNB()

model.fit(x_train, y_train)

result=model.score(x_test, y_test)
result*100

# import pickle
# pickle.dump(model, open('spam.pkl','wb'))
# model1 = pickle.load(open('spam.pkl','rb'))

def result(msg):
    data = [msg]
    vect = cv.transform(data).toarray()
    my_prediction = model.predict(vect)
    if my_prediction[0]==1:
        return "This is a Spam mail"
    else:
        return "This is not a Spam mail"
