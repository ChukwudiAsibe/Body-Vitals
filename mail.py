# import requests
# from datetime import datetime
# import Server

# firstName_given = Server.contact_form('firstName_given')
# lastName_given = Server.contact_form('lastName_given')
# email_given = Server.contact_form('email_given')
# country_selected = Server.contact_form('country_selected')
# subject = Server.contact_form('subject')
# message_given = Server.contact_form('message_given')


# def send_email():

#     import smtplib
    
#     EMAIL = 'chukwudiecommerce@gmail.com'
#     PASSWORD = 'qidr jnfk zgbs rong'
#     RECIPIENT = 'ec.asibe@imopoly.net'
#     SUBJECT = f"Doctor Alfred_{Server.subject}" 
#     TEXT = f'\n{Server.firstName_given}\t{Server.lastName_given}\
#             \n{Server.country_selected}\t{Server.email_given}\
#             \n{Server.message_given}'
#     MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(EMAIL, PASSWORD)
#     server.sendmail(EMAIL, RECIPIENT, MESSAGE)
#     # server.quit()
#     print('Mail Sent')





# post_api = 'https://api.sheety.co/575e93b17ed4b731cc7bd3a35a435457/emailTracking/sheet1'

# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# records = {

#     "sheet1": {
# 	  "first": Server.firstName_given,
#     "last": Server.lastName_given,
#     'date': today_date,
#     'time': now_time,
# 	  "email": Server.email_given,
#     "country": Server.country_selected,
#     "subject": Server.subject,
#     "message": Server.message_given
#   }
# }

# response = requests.post(post_api, json=records)
# print(response.status_code, response.text)
