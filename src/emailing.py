import smtplib

'''
Gmail:bot510project@gmail.com
PW:simtiaz1234 
'''

def sendmail(mail,message):
    smtpObj= smtplib.SMTP('smtp.gmail.com',587)
    r=smtpObj.ehlo()
    r=smtpObj.starttls()
    r=smtpObj.login('bot510project@gmail.com','simtiaz1234')
    r=smtpObj.sendmail('bot510project@gmail.com',mail,'Subject: checking our bot.\n\n You have a task pending')
    print r
