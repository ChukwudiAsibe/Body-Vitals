import streamlit as st
import joblib, time
import pandas as pd



st.image("resources/Image_Landing.jpg")
st.subheader("Give us the Test Data Lets Our AI Doctor Do the Evaluation.")
st.markdown("Here is Sample or test data to you can use to practice.")
st.dataframe(pd.read_csv('resources/sample_data.csv'))
gender = st.radio("Gender", options=('Male', 'Female'))
if gender == 'Male': gender = 1
else: gender = 0

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)

age = st.slider("Age", min_value=18, max_value=90, value=40)
hr = col1.slider("Heart Rate", min_value=60.0, max_value=100.0, value=50.0)
rr = col2.slider("Respiratory Rate", min_value=12.0, max_value=19.0, value=15.0)
bt = col3.slider("Body Temperature", min_value=36.0, max_value=37.5, value=36.5)
os = col4.slider("Oxygen Saturation", min_value=95.0, max_value=100.0, value=96.5)
sbp = col5.slider("Systolic Blood Pressure", min_value=110.0, max_value=140.0, value=120.0)
dbp = col6.slider("Diastolic Blood Pressure", min_value=70.0, max_value=90.0, value=80.0)
w = col7.slider("Weight (kg)", min_value=50.0, max_value=100.0, value=40.0)
h = col8.slider("Height (m)", min_value=1.0, max_value=2.0, value=1.5)

# Derivables
pp = sbp - dbp
bmi = w / (h*h)
dmap = dbp + ((1/3) * pp)

df = pd.DataFrame({ 
    "Heart Rate":[hr], 
    "Respiratory Rate":[rr],
    "Body Temperature":[bt],
    "Oxygen Saturation":[os],
    "Systolic Blood Pressure":[sbp],
    "Diastolic Blood Pressure":[dbp],
    "Age":[age],
    "Gender":[gender],
    "Weight (kg)":[w],
    "Height (m)":[h],
    # "Derived_HRV":[0.053200],
    "Derived_Pulse_Pressure":[pp],
    'Derived_BMI':[bmi],
    "Derived_MAP":[dmap]
    })

user_data = joblib.load('scaler_trained.pkl')
user_data = user_data.transform(df)

doctor = joblib.load('model_trained.pkl')
doctorAlfred = doctor.predict(user_data)[0]



def btn_clicked():
    # print("Yes Y did you click me")
    # st.write("Low Risk")
    pass

if st.button('Submit', key='submit', on_click=btn_clicked):
    bar = st.progress(0, text='Progress Report')
    for i in range(10):
        bar.progress((i+1)*10)
        time.sleep(0.5)
    st.write("Your Response")
    st.table(df)
    if doctorAlfred == "High Risk":
        st.write("Hi, I am Doctor Alfred. I Have Evaluated your report. I am Afraid your Body vitals is:")
        st.markdown(f"**{doctorAlfred}**")
    else:
        st.write("Hi, I am Doctor Alfred. I Have Evaluated your report. from the look of things, your Body vitals is:")
        st.markdown(f"**{doctorAlfred}**")