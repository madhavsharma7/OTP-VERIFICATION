import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
inapppassword=''
server.login('senderemailid',inapppassword)
try:
    otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
    msg = 'Hello!! PYTHON SEND YOU AN OTP YOUR OTP IS ' + str(otp)

except Exception as a:
    print(a)
sender = '' #senderemailid
receiver ='' #receiveremailid
server.sendmail(sender, receiver, msg)
print(msg)



