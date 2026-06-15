'''
import datetime
today=datetime.date.today()
future=today+datetime.timedelta(days=7)
print(future)



import datetime
day=datetime.date.today()
print(day.ctime())



import calendar
import datetime
today=datetime.date.today()
year=today.year
month=today.month
print(calendar.month(year,month))



import calendar
year=2026
print(calendar.calendar(year))
'''


import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

sender_mail="charansaibera4@gmail.com"
password="qjyilwwqquwtgcpm"
receiver_mail="samram5626@gmail.com"
target_time="10:24"

while True:
    current_time=datetime.now().strftime("%H:%M")

    if current_time==target_time:
        msg=EmailMessage()
        msg["Subject"]="Reminder"
        msg["From"]="charansaibera4@gmail.com"
        msg["To"]="samram5626@gmail.com"

        msg.set_content("This is autommated mail sent at the scheduled time.")

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
                smtp.login(sender_mail,password)
                smtp.send_message(msg)
            print("Email sent successfully!")
            break

        except Exception as e:
            print("Error :",e)
            break

    time.sleep(30)
                

        
    


