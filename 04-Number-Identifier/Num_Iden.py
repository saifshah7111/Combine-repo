def iden():
    a = float(input('Enter Number: '))
    if (a>0):
        print('Number is Positive')
    elif (a==0):
        print('Number is Zero')
    elif (a<0):
        print('Number is negative')
    else:
        print('Please enter a Number')    
iden()   
Yes_No = ''
while Yes_No != 'No' and Yes_No != 'N':
    print('-----------------------')
    Yes_No = str(input('Want to continue? : ')).title() 
    print('-----------------------')  
    if Yes_No == 'Yes' or Yes_No == 'Y':
        iden()
    elif Yes_No == 'No' or Yes_No == 'N':  
        print('Exit--')  
    else:
        print('Please enter Yes or No')    
