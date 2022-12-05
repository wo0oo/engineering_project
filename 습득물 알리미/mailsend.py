import smtplib
from email.mime.text import MIMEText
import time
from datetime import datetime, timedelta

user_mail=str(input("메일입력:"))
user_sec=int(input("분 입력:"))*60
start=time.time()


while True:
    NOW=datetime.now()
    Time_Info=NOW.strftime('%Y/%m/%d %H:%M:%S')
    MIN=Time_Info[14:16]
    SEC=Time_Info[17:19]
    # interval=timedelta(minutes=user_min)
    
    if int((time.time()-start)%user_sec)==0:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('lostarticle07@gmail.com','blnlfnaaieegbola')
        msg=MIMEText('본문')
        msg['Subject']='제목'
        s.sendmail("lostarticle07@gmail.com",user_mail,msg.as_string())
        s.quit()
