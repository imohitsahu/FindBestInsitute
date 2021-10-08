# Python code to illustrate Sending mail from  
# your Gmail account

import smtplib 



def sendMail(message , to):
	print('sendmail')
	print(to)
	print(message)
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("shrivastavasrishti82@gmail.com", "9516888232"); 
	s.sendmail("shrivastavasrishti82@gmail.com", to, message) 
	s.quit() 
	print('sent')


