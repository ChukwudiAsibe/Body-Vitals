import streamlit as st
import pandas as pd
import requests, re, smtplib, pycountry, time
from datetime import datetime
import joblib


st.title('Body vital tests')
st.divider()

evaluation = st.Page("evaluation.py", title="Evaluation")
about = st.Page("about.py", title="About")
insight = st.Page("insight.py", title="Insight")
contact = st.Page("contact.py", title="Contact")
blog = st.Page("blog.py", title="Blog")
ld = st.Page("limit_disclaimer.py", title="Disclaimer")

nav_pages = st.navigation([evaluation, about, insight, contact, blog, ld])
nav_pages.run()

# nav = st.sidebar.radio("Go to", ["Evaluate", "Insight", "About", "Limit and Disclaimer", "Contact", "Blog"], key='navigation bar')

# def form_click():
#     print('form_clicked')

# if nav == 'Evaluate':
#     st.image("C:/Users/CONIDSL00330/Desktop/ASIBE_DOCUMENT/Data Science CV/Pojects/Body Vitals/App_Dev/resources/Image_Landing.jpg")
#     st.subheader("Give us the Test Data Lets Our AI Doctor Do the Evaluation.")
#     st.markdown("Here is Sample or test data to you can use to practice.")
#     st.dataframe(pd.read_csv('resources/sample_data.csv'))
#     gender = st.radio("Gender", options=('Male', 'Female'))
#     if gender == 'Male': gender = 1
#     else: gender = 0

#     col1, col2 = st.columns(2)
#     col3, col4 = st.columns(2)
#     col5, col6 = st.columns(2)
#     col7, col8 = st.columns(2)

#     age = st.slider("Age", min_value=18, max_value=90, value=40)
#     hr = col1.slider("Heart Rate", min_value=60.0, max_value=100.0, value=50.0)
#     rr = col2.slider("Respiratory Rate", min_value=12.0, max_value=19.0, value=15.0)
#     bt = col3.slider("Body Temperature", min_value=36.0, max_value=37.5, value=36.5)
#     os = col4.slider("Oxygen Saturation", min_value=95.0, max_value=100.0, value=96.5)
#     sbp = col5.slider("Systolic Blood Pressure", min_value=110.0, max_value=140.0, value=120.0)
#     dbp = col6.slider("Diastolic Blood Pressure", min_value=70.0, max_value=90.0, value=80.0)
#     w = col7.slider("Weight (kg)", min_value=50.0, max_value=100.0, value=40.0)
#     h = col8.slider("Height (m)", min_value=1.0, max_value=2.0, value=1.5)

#     # Derivables
#     pp = sbp - dbp
#     bmi = w / (h*h)
#     dmap = dbp + ((1/3) * pp)

#     df = pd.DataFrame({ 
#         "Heart Rate":[hr], 
#         "Respiratory Rate":[rr],
#         "Body Temperature":[bt],
#         "Oxygen Saturation":[os],
#         "Systolic Blood Pressure":[sbp],
#         "Diastolic Blood Pressure":[dbp],
#         "Age":[age],
#         "Gender":[gender],
#         "Weight (kg)":[w],
#         "Height (m)":[h],
#         # "Derived_HRV":[0.053200],
#         "Derived_Pulse_Pressure":[pp],
#         'Derived_BMI':[bmi],
#         "Derived_MAP":[dmap]
#         })
    
#     user_data = joblib.load('scaler_trained.pkl')
#     user_data = user_data.transform(df)

#     doctor = joblib.load('model_trained.pkl')
#     doctorAlfred = doctor.predict(user_data)[0]
    
    

#     def btn_clicked():
#         # print("Yes Y did you click me")
#         # st.write("Low Risk")
#         pass

#     if st.button('Submit', key='submit', on_click=btn_clicked):
#         bar = st.progress(0, text='Progress Report')
#         for i in range(10):
#             bar.progress((i+1)*10)
#             time.sleep(0.5)
#         st.write("Your Response")
#         st.table(df)
#         if doctorAlfred == "High Risk":
#             st.write("Hi, I am Doctor Alfred. I Have Evaluated your report. I am Afraid your Body vitals is:")
#             st.markdown(f"**{doctorAlfred}**")
#         else:
#             st.write("Hi, I am Doctor Alfred. I Have Evaluated your report. from the look of things, your Body vitals is:")
#             st.markdown(f"**{doctorAlfred}**")

# elif nav == 'Insight':
#     st.image("C:/Users/CONIDSL00330/Desktop/ASIBE_DOCUMENT/Data Science CV/Pojects/Body Vitals/App_Dev/resources/Image_Landing.jpg")
#     st.image('resources/Visuals/newplot.png')
#     st.image('resources/Visuals/plot1.png')
#     st.image('resources/Visuals/plot2.png')

# elif nav == 'About':
#     st.image("C:/Users/CONIDSL00330/Desktop/ASIBE_DOCUMENT/Data Science CV/Pojects/Body Vitals/App_Dev/resources/Image_Landing.jpg")
#     st.subheader("Why Body Vital Tests Are Important")
#     st.markdown("Body vital tests, also known as vital signs monitoring, are performed to assess essential bodily functions and provide critical information about a person's health status. These tests help doctors, nurses, and healthcare professionals identify potential health problems, monitor ongoing conditions, and evaluate the effectiveness of treatments.")
#     st.markdown("**Early detection of health issues**: Abnormal vital signs can signal infections, cardiovascular problems, or respiratory distress early, allowing for timely intervention.")
#     st.markdown("**Monitoring chronic conditions**: For people with diseases such as diabetes, heart disease, or asthma, regular monitoring of vital signs helps keep track of their condition and adjust treatments as needed.")
#     st.markdown("**Evaluating treatment effectiveness**: Vital signs help assess whether a treatment, such as medication or oxygen therapy, is working.")
#     st.markdown("**Immediate response to emergencies**: In emergency situations, vital signs help healthcare providers quickly assess the severity of the condition and guide treatment decisions.")
#     st.markdown("Vital tests provide a quick, non-invasive way to assess overall health and are a critical part of any medical evaluation.")
#     st.markdown("""
#                 ### About Our AI-Powered Body Vital Evaluation Tool
#                 Our AI application provides an advanced solution for assessing body vitals, empowering users to monitor their health proactively. By analyzing key vital signs such as heart rate, blood pressure, and respiratory rate based on user inputs, the system evaluates potential health risks and provides immediate feedback. The application categorizes users into high-risk or low-risk groups, allowing them to make informed decisions about their well-being and seek medical attention when necessary.

#                 With the ability to detect subtle patterns that may indicate underlying health concerns, our AI aims to support early detection and prevention. Whether you are monitoring your vitals daily or using it during high-pressure situations, such as crises or emergency zones, this tool enhances personal and professional healthcare efforts.

#                 Designed for ease of use, the application delivers fast, accurate results, making it a valuable resource for individuals, healthcare workers, and humanitarian teams operating in remote or resource-limited environments.
#                 """)
# elif nav == 'Limit and Disclaimer':
#     st.subheader('AI Application Disclaimer (Experimental Use Only)')
#     st.markdown('This AI application is developed solely for experimental and research purposes. It is not intended for use in production environments or decision-making processes where data accuracy, reliability, or safety is critical. The AI system is provided "as is," without any guarantees or warranties of any kind, express or implied, including but not limited to the accuracy, completeness, or suitability for any particular purpose.')
#     st.markdown('##### Important Notices:')
#     st.markdown("""
#     - The application may produce unpredictable, incomplete, or erroneous outputs and should not be used in critical applications such as healthcare, financial services, or legal contexts.
#     - The dataset and models powering the application are experimental, and the results may not reflect real-world scenarios.
#     - Any use of this application is at the user’s sole risk. The developers are not responsible for any direct, indirect, incidental, or consequential damages resulting from the use of this application.
#     - Users must ensure compliance with applicable laws, ethical guidelines, and data protection regulations, especially when using sensitive or personal data in conjunction with the application.  
    
#     By using this AI application, you acknowledge and accept that it is intended for experimental purposes only and agree to assume full responsibility for any actions taken based on the outputs of this system.
#     """)
# elif nav == 'Blog':
#     st.image('resources/casualty.jpg')
#     st.subheader("How AI Can Help Healthcare Practitioners in War and Crisis Zones")
#     st.markdown('In war-torn regions or crisis zones, healthcare is often overwhelmed by the sheer number of patients and limited resources. Medical staff must operate under immense pressure, with the constant challenge of providing timely and effective care. In these high-stakes environments, Artificial Intelligence (AI) is becoming an essential tool to assist healthcare practitioners in improving patient outcomes, optimizing resource use, and saving lives. Here’s how AI can make a significant impact:')
#     st.markdown("""
#     1. **Efficient Triage and Prioritization**
    
#     AI can assist healthcare workers in war or crisis zones by automating the triage process, helping to identify which patients need immediate attention. In areas where medical staff are overburdened, AI systems can analyze vital signs—such as heart rate, oxygen levels, and blood pressure—enabling faster prioritization of critical patients.
#     - **AI-Driven Triage Algorithms:** AI can instantly assess incoming patients’ vitals and medical histories to assign urgency scores. This means that life-threatening cases like traumatic injuries or respiratory failure are detected immediately, allowing limited resources to be allocated to those most in need.
#     - **Portable Devices:** Wearable or handheld devices powered by AI can be used in the field to collect data from multiple patients simultaneously. This minimizes delays in treatment and ensures rapid response to severe cases.
    
#     2. **Remote Patient Monitoring**
                
#     In crisis zones, healthcare infrastructure is often compromised, making it difficult to monitor patients regularly. AI-based remote monitoring solutions can play a crucial role by continuously tracking patients' vital signs and alerting healthcare teams to deteriorating conditions.
#     - **Real-Time Alerts:** AI systems can be used to monitor patients in makeshift hospitals or refugee camps, offering real-time alerts when a patient’s condition worsens. This allows doctors to provide immediate intervention, even when they are not physically present.
#     - **Telemedicine Support:** AI can be integrated into telemedicine platforms, allowing healthcare workers to collaborate with remote experts. This is particularly useful in conflict zones where access to specialists may be limited.          

#     3. **Resource Optimization**
                
#     One of the key challenges in war or crisis zones is the scarcity of medical supplies, staff, and facilities. AI helps optimize the use of these limited resources by analyzing real-time data and predicting future needs.   
#     - **Resource Allocation Models:** AI can forecast which patients are likely to require more intensive care, such as ventilators, based on their body vitals and historical data. This ensures that critical equipment is available when needed, reducing waste and improving patient outcomes.         
#     - **Supply Chain Management:** AI-driven analytics can predict shortages in medical supplies like medications, surgical tools, or blood donations. This predictive ability ensures healthcare facilities are stocked according to demand, minimizing shortages and improving patient care.

#     4. **Predictive Analytics for Early Intervention**
    
#     AI systems are capable of predictive analysis by identifying subtle changes in vital signs before a crisis occurs. This is particularly important in crisis zones, where early detection of life-threatening conditions can prevent catastrophic outcomes.

#     - **Sepsis Detection:** AI models trained on data from previous cases can detect early signs of sepsis, a condition that is difficult to diagnose and has a high mortality rate if left untreated. AI alerts doctors to intervene before the condition escalates.

#     - **Predicting Infectious Disease Outbreaks:** In crisis zones, disease outbreaks can escalate quickly. AI systems can monitor patient data to predict outbreaks of contagious diseases by identifying early patterns in vital signs, such as fevers or respiratory issues, allowing healthcare teams to take preventative action.
    
#     5. **Portable AI for On-The-Go Diagnosis**
                
#     AI-powered portable diagnostic tools can be a lifeline in areas where hospital infrastructure has been destroyed or where medical personnel are scarce. These devices allow healthcare providers to make real-time diagnoses in the field, without needing advanced medical equipment.

#     - **Handheld Diagnostic Devices:** Handheld AI devices can analyze vital signs, detect injuries, and diagnose infections. This helps mobile healthcare teams to provide care on-site without transporting patients to overwhelmed hospitals.

#     - **AI in Imaging and Diagnostics:** Portable imaging devices, supported by AI algorithms, can help healthcare workers quickly identify injuries like fractures or internal bleeding. This minimizes delays in care and allows for immediate action in the field.

#     6. **Mental Health Monitoring**
                
#     Beyond physical health, AI can play a role in monitoring the mental well-being of individuals in crisis zones, especially children, refugees, and combatants who are more vulnerable to trauma.

#     - **Tracking Stress and PTSD:** AI models can analyze heart rate variability (HRV) and other vital signs to monitor stress levels in individuals exposed to traumatic events. Early detection of stress or PTSD can allow healthcare workers to provide timely mental health interventions.

#     - **Mobile Mental Health Apps:** AI-driven mental health applications can offer remote counseling and therapeutic support, ensuring that individuals in crisis zones have access to psychological care even when professional mental health practitioners are not available on-site.           
    
#     7. **AI-Powered Data Aggregation for Crisis Management**
                
#     AI systems can aggregate large datasets from multiple patients, giving healthcare organizations the ability to understand broader trends in health data. This can guide crisis response strategies and public health interventions.

#     - **Predictive Modeling for Healthcare Planning:** AI can provide governments and humanitarian organizations with insights on potential outbreaks, resource needs, or hotspots of illness. This helps in planning and mobilizing medical units efficiently.

#     - **Tracking Population Health:** AI systems can track health trends across populations in refugee camps or displaced communities. These insights help healthcare providers identify emerging issues and allocate resources accordingly.            
    
#     #### Conclusion
#     In war-torn regions and crisis zones, AI has the potential to revolutionize the way healthcare practitioners deliver care. By providing rapid health assessments, optimizing resource use, and predicting life-threatening conditions, AI can save countless lives in places where medical infrastructure is scarce and human resources are stretched thin. As AI technology advances, its applications in these high-pressure environments will only expand, offering new ways to protect and improve the health of individuals in some of the world’s most vulnerable areas.

#     Ultimately, AI is not a replacement for human healthcare providers but a powerful tool that enhances their capabilities, allowing them to work more efficiently and effectively in the most challenging conditions.
                
#     """)



# else:
#     # Get a list of all countries
#     countries = ["Select"]
#     for country in pycountry.countries:
#         countries.append(country.name)

#     st.image("C:/Users/CONIDSL00330/Desktop/ASIBE_DOCUMENT/Data Science CV/Pojects/Body Vitals/App_Dev/resources/Image_Landing.jpg")
    
#     st.divider()

#     st.subheader("We’d Love to Hear from You!")
#     col1, col2 = st.columns(2)
#     col2.image("resources/contact_image.jpg")
#     col1.markdown("Whether you have a question, need support, comments, recommendation or want to share feedback, we’re here to help. Please feel free to reach out through the form below or use the contact information provided. We aim to respond as quickly as possible to ensure your experience with us is exceptional.", unsafe_allow_html=True)

#     st.divider()

#     col1, col2 = st.columns(2)
#     col3, col4 = st.columns(2)

#     # Function to check if input is a valid email
#     def is_valid_email(email):
#         # Regular expression for validating an email
#         email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
#         return re.match(email_pattern, email)

#     with st.form(key='form1'):
#         firstName_given = col1.text_input(label='First Name', placeholder='Barack', key='firstName_given')
#         lastName_given = col2.text_input(label='Last Name', placeholder='Obama', key='lastName_given')
#         email_given = col3.text_input(label='Email', placeholder='doctor@ai.com', key='email_given')
#         country_selected = col4.selectbox("Country", options=countries, key='country_selected')
#         subject = st.text_input('Subject', placeholder='Subject', key='subject')
#         message_given = st.text_area("Comment or Message", placeholder='Write your Message', key='message_given')
#         if st.form_submit_button('Send'):
#             # Check if the user input is empty
#             if not firstName_given:
#                 st.warning("First Name is required.", icon="🚨")
#             elif not lastName_given:
#                 st.warning("Last Name is required.", icon="🚨")  
#             elif not email_given:
#                 st.warning("Email is required.", icon="🚨")
#             elif not is_valid_email(email_given):
#                 st.warning("Invalid Email.", icon="🚨")
#             elif not country_selected or country_selected == "Select":
#                 st.warning("Country is required.", icon="🚨")
#             elif not subject:
#                 st.warning("Subject is required.", icon="🚨")
#             elif not message_given:
#                 st.warning("Massage is required.", icon="🚨")
#             else:
#                 EMAIL = 'chukwudiecommerce@gmail.com'
#                 PASSWORD = 'qidr jnfk zgbs rong'
#                 RECIPIENT = 'ec.asibe@imopoly.net'
#                 SUBJECT = f"Doctor Alfred_{subject}" 
#                 TEXT = f'\n{firstName_given}\t{lastName_given}\
#                         \n{country_selected}\t{email_given}\
#                         \n{message_given}'
#                 MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

#                 server = smtplib.SMTP('smtp.gmail.com', 587)
#                 server.starttls()
#                 server.login(EMAIL, PASSWORD)
#                 server.sendmail(EMAIL, RECIPIENT, MESSAGE)

#                 post_api = 'https://api.sheety.co/575e93b17ed4b731cc7bd3a35a435457/emailTracking/sheet1'

#                 today_date = datetime.now().strftime("%d/%m/%Y")
#                 now_time = datetime.now().strftime("%X")

#                 records = {

#                     "sheet1": {
#                     "first": firstName_given,
#                     "last": lastName_given,
#                     'date': today_date,
#                     'time': now_time,
#                     "email": email_given,
#                     "country": country_selected,
#                     "subject": subject,
#                     "message": message_given
#                 }
#                 }

#                 response = requests.post(post_api, json=records)
#                 print(response.status_code, response.text)

#                 st.success(f"Hello, {firstName_given}! Your Message was Successfuly sent")
#                 st.write('We am pretty sure you want to reach the team lead on LinkedIn')
#                 st.markdown("""
#                 <a href="https://www.linkedin.com/in/emmanuel-asibe-19846117a/" target="_blank">I am on LinkedIn</a>
#                 """, unsafe_allow_html=True)