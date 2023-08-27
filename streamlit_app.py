import numpy as np
import pickle
import pandas as pd

import streamlit as st

## LOAD THE MODELS
model=pickle.load(open('model.pkl', 'rb'))
scalar=pickle.load(open('scaling.pkl', 'rb'))

def prediction_price(CRIM,ZN,INDUS,CHAS,NOX,RM,Age,DIS,RAD,TAX,PTRATIO,B,LSTAT):

    prediction= model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,Age,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
    print(prediction)
    return prediction

def main ():
    st.title("Boston house pricing")
    html_temp = """
    <div style="background-color: tomato; padding:10px">
    <h2 style="color: white; text-align:center;">Streamlit Boston house Pricing ML App </h2>
    </div>
    """
    st.markdown (html_temp, unsafe_allow_html=True)
    CRIM = st.text_input ("CRIM",)
    ZN = st.text_input("ZN", )
    INDUS = st.text_input ("INDUS",)
    CHAS = st.text_input ("CHAS", )
    NOX = st.text_input ("NOX", )
    RM = st.text_input ("RM", )
    Age = st.text_input ("Age", )
    DIS = st.text_input ("DIS", )
    RAD = st.text_input ("RAD", )
    TAX = st.text_input ("TAX", )
    PTRATIO = st.text_input ("PTRATIO", )
    B = st.text_input ("B", )
    LSTAT = st.text_input ("LSTAT", )
   
    
    output=""
    if st.button("Predict"):
        data = prediction_price(CRIM,ZN,INDUS,CHAS,NOX,RM,Age,DIS,RAD,TAX,PTRATIO,B,LSTAT)
        final_input = scalar.transform(np.array(data).reshape(1,-1))
        output=model.predict(final_input)[0]
    st.success('The Price is {}'.format(output))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
        
if __name__ == '__main__':
        main()