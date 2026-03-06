import streamlit as st
import joblib
import numpy as np

model = joblib.load("model_c.pkl")
st.set_page_config(page_title="Car Price Prediction", layout="wide")
st.title("🚗 Car Price Prediction App (Full Version)")
st.write("Please enter all 26 specifications to get an accurate price prediction.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    symboling = st.number_input("Symboling (-3 to 3)", value=0)
    fueltype = st.selectbox("Fuel Type", ["gas", "diesel"])
    aspiration = st.selectbox("Aspiration", ["std", "turbo"])
    doornumber = st.selectbox("Door Number", ["two", "four"])
    carbody = st.selectbox("Car Body", ["sedan", "hatchback", "wagon", "hardtop", "convertible"])
    drivewheel = st.selectbox("Drive Wheel", ["fwd", "rwd", "4wd"])
    enginelocation = st.selectbox("Engine Location", ["front", "rear"])
    wheelbase = st.number_input("Wheelbase", value=98.0)
    carlength = st.number_input("Car Length", value=170.0)

with col2:
    carwidth = st.number_input("Car Width", value=65.0)
    carheight = st.number_input("Car Height", value=53.0)
    curbweight = st.number_input("Curb Weight", value=2500)
    enginetype = st.selectbox("Engine Type", ["dohc", "ohcv", "ohc", "l", "rotor", "ohcf", "dohcv"])
    cylindernumber = st.selectbox("Cylinder Number", ["four", "six", "five", "eight", "two", "three", "twelve"])
    enginesize = st.number_input("Engine Size", value=120)
    fuelsystem = st.selectbox("Fuel System", ["mpfi", "2bbl", "mfi", "1bbl", "spfi", "4bbl", "idi", "spdi"])
    boreratio = st.number_input("Bore Ratio", value=3.3)
    stroke = st.number_input("Stroke", value=3.2)

with col3:
    compressionratio = st.number_input("Compression Ratio", value=10.0)
    horsepower = st.number_input("Horsepower", value=100)
    peakrpm = st.number_input("Peak RPM", value=5000)
    citympg = st.number_input("City MPG", value=25)
    highwaympg = st.number_input("Highway MPG", value=30)
    

fueltype_enc = 1 if fueltype == "diesel" else 0
aspiration_enc = 1 if aspiration == "turbo" else 0
door_enc = 1 if doornumber == "four" else 0

drivewheel_map = {"fwd": 0, "rwd": 1, "4wd": 2}
drive_enc = drivewheel_map[drivewheel]


features = np.array([[
    symboling,fueltype_enc, aspiration_enc,
    door_enc, 0, drive_enc, 0, wheelbase, 
    carlength, carwidth, carheight, curbweight, 0,
    0, enginesize, 0, boreratio, stroke,
    compressionratio, horsepower, peakrpm, citympg, highwaympg
]])


st.divider()

if st.button("Predict Car Price"):
    try:
        prediction = model.predict(features)
        price = abs(np.array(prediction).item())
        st.balloons()
        st.write("### Predicted Price:")
        st.header(f"$ {price}") 
        
    except Exception as e:
        st.error(f"Error: {e}")