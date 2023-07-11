import streamlit as st
from Disease_predict import show_predict_page

   # Use st.markdown with CSS styling
st.markdown(
    """
    <style>
    .my-markdown {
        background-color: #f1f1f1;
        padding-left: 30px;
        padding-right: 30px;
        padding-top: 10px;
        padding-bottom: 10px;
        margin-bottom: 50px;
        font-family: Georgia;
        font-size: 14pt;}
    </style>
    """,
    unsafe_allow_html=True
)


with st.sidebar:
    st.title("Main Menu")
    selected_option = st.selectbox("Go to", ("Home", "Disease Prediction", "Test Prediction"))
    
if selected_option == "Home":
    # Show home content
    st.markdown(' # Welcome to home page')
    st.markdown(' ### Objectives')
    st.markdown("<div class='my-markdown'>1.This is a machine learning-based disease detection system that utilizes laboratory test results for accurate diagnosis.</div>", unsafe_allow_html=True)
    st.markdown("<div class='my-markdown'>2.It is designes and implemented a user-friendly web application interface for seamless interaction with the disease detection system.</div>", unsafe_allow_html=True)
    st.markdown("<div class='my-markdown'>3.It enable users to input their symptoms and receive predictions for relevant laboratory tests that can aid in further diagnosis.</div>", unsafe_allow_html=True)    
    
    st.markdown(' ### Information about inputs')
    
    
    
elif selected_option == "Disease Prediction":
    # Show disease prediction content
    st.markdown(' # Disease Detection Page')
    
# Apply the CSS class to the markdown text
    st.markdown("<div class='my-markdown'>Here you can Diagnose if you have Hepatitis C, Fiborosis or Cirrhosis, with certain labarotary reports values you provide as input.</div>", unsafe_allow_html=True)
    
    show_predict_page()
elif selected_option == "Test Prediction":
    # Show test prediction content
    st.header("Test Prediction")
    st.write("Perform test prediction here.")