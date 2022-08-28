import base64
from distutils.log import fatal
from pickletools import optimize
# from tkinter import N
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Credit Card Default Payment For Next Month Prediction Home",
    page_icon="🏠",
)

with st.sidebar:
    choose = option_menu("Payment Default", ["Home", "Data",  "Code", "Contact"],
                         icons=['house', 'gem','clipboard-data', 
                                'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={"container": {"padding": "5!important", "background-color": "#0E1117"},
                                 "icon": {"color": "orange", "font-size": "25px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#262730"},
                                 "nav-link-selected": {"background-color": "#FF4B4B"},
                                 }
                         )

if choose == "Home":
    st.markdown(''' 
                # Credit Card Default Prediction

    ''', True)

#image=Image.open("Card.jpg")
#st.image(image,use_column_width=True)

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

    st.write("Enter The Repayment Status  -1=Pay Duly ,  1=Payment Delay For One Month & So On")

    col5,col6,col7 =st.columns(3)  

    with col5:
        PAY_0=st.number_input(label="Current Month",min_value=-2,max_value=8)

    with col6:
        PAY_2=st.number_input(label="Last Month", min_value=-2 , max_value=9)

    with col7:
        PAY_3=st.number_input(label="Last Before Month",min_value=-2,max_value=10)

    st.write("Amount Of The Bill Statement ")
    col8,col9,col10=st.columns(3)

    with col8:
        BILL_AMT1=st.number_input(label="Current Month",min_value=0,max_value=1000000)

    with col9:
        BILL_AMT2=st.number_input(label="Last Month",min_value=0,max_value=1000001)

    with col10:
        BILL_AMT3=st.number_input(label="Last Before Month",min_value=0,max_value=1000002)

    st.write("Amount Of The Pervious Payment")
    col11,col12,col13=st.columns(3)

    with col11:
        PAY_AMT1=st.number_input(label="Current Month.",min_value=0,max_value=1000000)

    with col12:
        PAY_AMT2=st.number_input(label="Last Month..",min_value=0,max_value=1000001)

    with col13:
        PAY_AMT3=st.number_input(label="Last Before Month...",min_value=0,max_value=1000002)

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
    if prediction==0:
        _prediction="Not Default"
    else:
        _prediction="Default"    
    if st.button("Predict"):
         st.write(('The Person Will Be') ,(_prediction))
      
    # st.subheader("If Prediction Is 1 Then Person Will Be Default Payment For Next Month")
    # st.subheader("If Prediction Is 0 Then Person Will Not Be Default Payment For Next Month")

if choose == "Data":

    data = pd.read_excel("creditcarddefault.xlsx")
    st.dataframe(data, width=800, height=800)

if choose == "Code":
    st.header("Notebook")
    HtmlFile = open("Credit_Card_Default-Final.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=9500, width=800)


if choose=="Contact":
    st.header("Contact Details")
    st.subheader("Heroku Link")
    st.write("csdg")
    st.subheader("GitHub Link")
    st.write("Link")