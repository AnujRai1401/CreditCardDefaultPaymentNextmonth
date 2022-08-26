from array import array
from email.mime import image
import streamlit as st
import numpy as np
import pickle
from PIL import Image

st.title('Credit Card Default Prediction')

image=Image.open("Card.jpg")
st.image(image,use_column_width=True)

# col1,col2 =st.columns(2)

LIMIT_BAL=st.number_input(label="Enter The Card Limit Balance",min_value=0,max_value=1000000)

col1,col2,col3,col4 =st.columns(4)

with col1:
    SEX=st.selectbox("Select Your Gender",("Male","Female"))

with col2:
    EDUCATION=st.selectbox("Select Your Education",("Graduate School","University","High school","Other"))    

with col3:
    MARRIAGE=st.selectbox("Marital Status",("Married","Single","Others"))    

with col4:
    AGE=st.number_input(label="Enter Your Age",min_value=21,max_value=79)    

col5,col6,col7 =st.columns(3)  

with col5:
    PAY_0=st.number_input(label="Enetr The Repayment Status",min_value=-2,max_value=8)

with col6:
    PAY_2=st.number_input(label="Enter The Repayment Status", min_value=-2 , max_value=9)

with col7:
    PAY_3=st.number_input(label="Enter The Repayment Status",min_value=-2,max_value=10)


col8,col9,col10=st.columns(3)

with col8:
    BILL_AMT1=st.number_input(label="Amount Of Bill Statement",min_value=0,max_value=1000000)

with col9:
    BILL_AMT2=st.number_input(label="Amount Of Bill Statement",min_value=0,max_value=1000001)

with col10:
    BILL_AMT3=st.number_input(label="Amount Of Bill Statement",min_value=0,max_value=1000002)

col11,col12,col13=st.columns(3)

with col11:
    PAY_AMT1=st.number_input(label="Amount Of Pervious Payment",min_value=0,max_value=1000000)

with col12:
    PAY_AMT2=st.number_input(label="Amount Of Pervious Payment",min_value=0,max_value=1000001)

with col13:
    PAY_AMT3=st.number_input(label="Amount Of Pervious Payment",min_value=0,max_value=1000002)

if SEX == "Male":
    _SEX = 1
else:
    _SEX = 2

if EDUCATION == "Graduate School":
    _EDUCATION = 1
elif EDUCATION == "University":
    _EDUCATION = 2
elif EDUCATION == "High chool":
    _EDUCATION = 3
else: 
    _EDUCATION = 4

   
if MARRIAGE == "Married":
    _MARRIAGE = 1
elif MARRIAGE == "Single":
    _MARRIAGE = 2
else:
    _MARRIAGE = 3       

inputs=np.array([[LIMIT_BAL,_SEX,_EDUCATION,_MARRIAGE,AGE,PAY_0,PAY_2,PAY_3,BILL_AMT1,BILL_AMT2,BILL_AMT3,PAY_AMT1,PAY_AMT2,PAY_AMT3]])

with open ('RF1.pickle','rb') as f:
    model=pickle.load(f)

prediction = model.predict(inputs)  

if st.button("Predict"):
    st.write('You will be'),(prediction)
