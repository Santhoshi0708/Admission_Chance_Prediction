#Chance of Admission for Higher Studies 
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Reading the data from user as a csv file
Admission_Chance=pd.read_csv('Dataset.csv')

X=Admission_Chance[['GRE Score', 'TOEFL Score', 'University Rating', ' SOP',
       'LOR ', 'CGPA', 'Research']]
y = Admission_Chance['Chance of Admit ']

#Features of Student to a graduate Program
Feature1=st.number_input('GRE Score 290 to 340')
Feature2 =st.number_input('TOEFL Score 92 to 120')
Feature3=st.number_input('University Rating 1 to 5')
Feature4=st.number_input('SOP 1 to 5')
Feature5=st.number_input('LOR 1 to 5')
Feature6=st.number_input('CGPA 6.6 to 9.92')
Feature7=st.number_input('Research 0 to 1')

#Training and testing the splited data
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.8, random_state=2529)
#call function to the selected model
model=LinearRegression()

#fits the data to the splited data
model.fit(X_train,y_train)
#user input for predicting the data
Input=[Feature1,Feature2,Feature3,Feature4,Feature5,Feature6,Feature7]

#A button to predict the data https://www.linkedin.com/in/kothapalli-santhoshi-368951254/
if st.button("Predict"):
    A=model.predict([ Input ])*100
    st.write(f"The Admission Chance is { A[0]:.2f}%")
