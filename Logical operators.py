good_credit= True
criminal_record= True

if good_credit and not criminal_record:
 print("eligble for loan")

else: 
 print('Sorry you are not eligible')


#Creating fill in form

Full_name = input('Please Enter Your Full Name:')

if len(Full_name) <  3 or len(Full_name) > 10 :
 print('Name should be bigger than 3 char and less than 10 char')

elif len(Full_name) > 10:
 print('Name should be less that 10 characters')

else:
 print('Name looks good')
