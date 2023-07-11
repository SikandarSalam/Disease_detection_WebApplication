import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data= pickle.load(file)
    return data

data= load_model()




linear_Reg= data['model']
le_Category= data['le_Category']
le_sex= data['le_sex']

def show_predict_page():

    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.number_input("Enter your age", min_value=0, max_value=100, value=25)
        gender = st.text_input("Enter your Gender", placeholder="m or f")
        alb = st.number_input("Enter your Albumin Level(ALB)", step=0.01,min_value=0.0, max_value=50.0, value=24.5)
        alp = st.number_input("Enter your Alkaline phosphate Level(ALP)", step=0.01,min_value=30.0, max_value=90.0, value=52.5)
    with col2:
        alt = st.number_input("Enter your Alanine transaminase(ALT)", step=0.01,min_value=0.0, max_value=100.0, value=32.6)
        ast = st.number_input("Enter your Aspartate aminotransferase(AST)", step=0.01,min_value=15.0, max_value=200.0, value=22.6)
        bil = st.number_input("Enter your Bilurubin(BIL)", step=0.01,min_value=0.0, max_value=40.0, value=18.6)
        che = st.number_input("Enter your Serum cholinesterase(CHE)", step=0.01,min_value=0.0, max_value=20.0, value=12.6)
    with col3:
        chol = st.number_input("Enter your Cholestorol(CHOL)", step=0.01,min_value=0.0, max_value=10.0, value=8.6)
        crea = st.number_input("Enter your Creatinine(CREA)", min_value=70, max_value=110, value=85)
        ggt = st.number_input("Enter your Gamma-glutamyl transpeptidase(GGT)", step=0.01,min_value=0.0, max_value=60.0, value=32.6)
        prot = st.number_input("Enter your Total Protein(PROT)", step=0.01,min_value=50.0, max_value=100.0, value=69.6)
    ok = btn= st.button("Diagnose")
    if ok:
        x = np.array([[age, gender, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot ]])
        x[:,1]= le_sex.transform(x[:, 1])
        x= x.astype(float)
        
        output= linear_Reg.predict(x)
        
        if output<=0 and output <=0.5:
            health="Normal"
        elif output>0.5 and output<=0.7:
            health= "Hepatotis C"
        elif output>0.7 and output<=0.9:
            health="Fibrosis"
        else:
            health="Cirhosis"
        
        st.success(f"You have been diagnosed {health}")

    