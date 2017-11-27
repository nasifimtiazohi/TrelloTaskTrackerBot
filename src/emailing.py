import smtplib
import os

gmailid=os.environ.get("GMAIL_ID")
gmailpass=os.environ.get("GMAIL_PASS")

def sendmail(mail,message):
    smtpObj= smtplib.SMTP('smtp.gmail.com',587)
    r=smtpObj.ehlo()
    r=smtpObj.starttls()
    r=smtpObj.login(gmailid,gmailpass)
    r=smtpObj.sendmail('bot510project@gmail.com',mail,'Subject: Nagging Reminder.\n\n'+message)
    print r

if __name__=="__main__":
    #just for testing
    sendmail("sads","SADSD")
