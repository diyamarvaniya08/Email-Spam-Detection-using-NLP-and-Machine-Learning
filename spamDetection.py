import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st


data= pd.read_csv("C:\Email Spam Detection ML Model Project\spam.csv")
print(data.head())
print(data.shape)


#drop suplicates from data
data.drop_duplicates(inplace=True)
print(data.shape)


# check for null in data
print(data.isnull().sum())


# rename columns
data['Category']= data['Category'].replace(['ham', 'spam'], ['Not Spam', 'Spam'])
print(data.head())



# split data in train and test sets
mess= data['Message']
cat= data['Category']

(mess_train, mess_test, cat_train, cat_test) = train_test_split(mess, cat, test_size= 0.2)



cv= CountVectorizer(stop_words= 'english')
features= cv.fit_transform(mess_train)


#creat model

model= MultinomialNB()
model.fit(features, cat_train)

#test model
features_test= cv.transform(mess_test)
accuracy= model.score(features_test, cat_test)
print("MOdel Accuracy:", accuracy*100, "%")


#predict data (for example)
message= cv.transform(['Congratulations, you won a lottery']).toarray()
result= model.predict(message)
print(result)


# using function predict data (for example)
def predict(message):
    input_message= cv.transform([message]).toarray()
    result= model.predict(input_message)
    return result

output= predict('Congratulations, you won a lottery')
print(output)



# creating web app using streamlit
     
     # streamlit run spamDetection.py  (for checking run it in terminal)


def predict(message):
    input_message= cv.transform([message]).toarray()
    result= model.predict(input_message)
    return result

st.header('Spam Detection')

Input_Message= st.text_input('Enter Message Here')

if st.button('validate'):
    output= predict(Input_Message)
    st.markdown(output)


