import pickle
import streamlit as st
import numpy as np

loaded_model = pickle.load(open('rainfall_trained_model.pkl','rb'))
model = loaded_model["model"]
feature_name = loaded_model["feature_name"]

def rainfall_prediction(input_data):
    np_as_array = np.asarray(input_data)
    input_reshaped = np_as_array.reshape(1,-1)
    prediction = model.predict(input_reshaped)
    return 'No Rainfall' if prediction[0] == 0 else 'Rainfall'

def main():
    st.set_page_config(page_title="Rainfall Predictor", page_icon="🌦️", layout="centered")

    st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        text-align: center;
        color: #1f77b4;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-size: 1rem;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #105288;
    }
    .stNumberInput>div>input {
        border-radius: 0.5rem;
        padding: 0.4rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>🌦️ Rainfall Predictor</h1>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pressure = st.number_input('Pressure', format="%.2f")
        Humidity = st.number_input('Humidity', format="%.2f")
        Winddirection = st.number_input('Wind Direction', format="%.2f")
    with col2:
        Dewpoint = st.number_input('Dewpoint', format="%.2f")
        Cloud = st.number_input('Cloud', format="%.2f")
        Windspeed = st.number_input('Wind Speed', format="%.2f")
    with col3:
        Sunshine = st.number_input('Sunshine', format="%.2f")

    st.markdown("---")

    if st.button("Predict Rainfall"):
        try:
            input_values = [Pressure, Dewpoint, Humidity, Cloud, Sunshine, Winddirection, Windspeed]
            prediction = rainfall_prediction(input_values)
            if prediction == "Rainfall":
                st.markdown(f"<h2 style='color:#d62728; text-align:center;'>🌧️ {prediction}</h2>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h2 style='color:#2ca02c; text-align:center;'>☀️ {prediction}</h2>", unsafe_allow_html=True)
        except ValueError:
            st.markdown("<h3 style='color:#ff7f0e; text-align:center;'>⚠️ Please enter valid numeric values!</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
