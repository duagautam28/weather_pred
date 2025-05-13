import streamlit as st
import pickle

st.title("Weather Prediction App.......")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter max temperature")
mint=st.number_input("Enter min temperature")
w=st.number_input("Enter windspeed")
button=st.button("Predict")
if button:
    lr=pickle.load(open('wp.pkl','rb'))
    result=lr.predict([[pn,maxt,mint,w]])[0]
    st.markdown(f"today weather situation is {result}")

    

