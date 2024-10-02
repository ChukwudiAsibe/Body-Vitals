import streamlit as st
import requests, re, smtplib, pycountry, time
from datetime import datetime

 # Get a list of all countries
countries = ["Select"]
for country in pycountry.countries:
    countries.append(country.name)

st.image("resources/Image_Landing.jpg")

st.divider()

st.subheader("We’d Love to Hear from You!")
col1, col2 = st.columns(2)
col2.image("resources/contact_image.jpg")
col1.markdown("Whether you have a question, need support, comments, recommendation or want to share feedback, we’re here to help. Please feel free to reach out through the form below or use the contact information provided. We aim to respond as quickly as possible to ensure your experience with us is exceptional.", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Function to check if input is a valid email
def is_valid_email(email):
    # Regular expression for validating an email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email)

with st.form(key='form1'):
    firstName_given = col1.text_input(label='First Name', placeholder='Barack', key='firstName_given')
    lastName_given = col2.text_input(label='Last Name', placeholder='Obama', key='lastName_given')
    email_given = col3.text_input(label='Email', placeholder='doctor@ai.com', key='email_given')
    country_selected = col4.selectbox("Country", options=countries, key='country_selected')
    subject = st.text_input('Subject', placeholder='Subject', key='subject')
    message_given = st.text_area("Comment or Message", placeholder='Write your Message', key='message_given')
    if st.form_submit_button('Send'):
        # Check if the user input is empty
        if not firstName_given:
            st.warning("First Name is required.", icon="🚨")
        elif not lastName_given:
            st.warning("Last Name is required.", icon="🚨")  
        elif not email_given:
            st.warning("Email is required.", icon="🚨")
        elif not is_valid_email(email_given):
            st.warning("Invalid Email.", icon="🚨")
        elif not country_selected or country_selected == "Select":
            st.warning("Country is required.", icon="🚨")
        elif not subject:
            st.warning("Subject is required.", icon="🚨")
        elif not message_given:
            st.warning("Massage is required.", icon="🚨")
        else:
            EMAIL = st.secrets["EMAIL"]
            PASSWORD = st.secrets["PASSWORD"]
            RECIPIENT = st.secrets["RECIPIENT"]
            SUBJECT = f"Doctor Alfred_{subject}" 
            TEXT = f'\n{firstName_given}\t{lastName_given}\
                    \n{country_selected}\t{email_given}\
                    \n{message_given}'
            MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, RECIPIENT, MESSAGE)

            post_api = 'https://api.sheety.co/575e93b17ed4b731cc7bd3a35a435457/emailTracking/sheet1'

            today_date = datetime.now().strftime("%d/%m/%Y")
            now_time = datetime.now().strftime("%X")

            records = {

                "sheet1": {
                "first": firstName_given,
                "last": lastName_given,
                'date': today_date,
                'time': now_time,
                "email": email_given,
                "country": country_selected,
                "subject": subject,
                "message": message_given
            }
            }

            response = requests.post(post_api, json=records)
            print(response.status_code, response.text)

            st.success(f"Hello, {firstName_given}! Your Message was Successfuly sent")
            st.write('We am pretty sure you want to reach the team lead on LinkedIn')
            st.markdown("""
            <a href="https://www.linkedin.com/in/emmanuel-asibe-19846117a/" target="_blank">I am on LinkedIn</a>
            """, unsafe_allow_html=True)