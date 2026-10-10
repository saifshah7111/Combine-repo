def calc():
    a = int(input('Enter Number: '))
    x = input('Enter Operator: ')
    b = int(input('Enter Number: '))
    if x == '+':
        print (a,' + ', b ,' = ',a+b)
    elif x == '-':
        print (a,' - ', b ,' = ',a-b)  
    elif x == '×':
        print (a,' × ', b ,' = ',a*b)
    elif x == '÷':
        print (a,' ÷ ', b ,' = ',a/b)     
    else: 
        print('Please enter the following operators (+,-,×,÷)')
calc() 
print('----------------')       
Yes_No = ""
while Yes_No != "No" and Yes_No != 'N':
    Yes_No = str(input('Want to continue? : ')).title()
    if Yes_No == 'Yes' or Yes_No == 'Y':
        calc()
    elif Yes_No == 'No' or Yes_No == 'N':
        print('Exit---')    
    else:
        print('Please enter Yes or No') 
