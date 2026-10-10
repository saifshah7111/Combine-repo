def calc():
    a = int(input('Enter Number: '))
    print("")
    x = ''
    while x != '+' and x != '-' and x != '×' and x != '÷' :
        x = input('Enter Operator: ')
        if x == '+' or x == '-' or x == '×' or x == '÷':
            print("")
        else:
            print('Please enter the following operators (+,-,×,÷)')
    b = int(input('Enter Number: '))
    print("")
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
    print('----------------')      
calc() 
     
Yes_No = ""
while Yes_No != "No" and Yes_No != 'N':
    Yes_No = str(input('Want to continue? : ')).title()
    print('----------------')  
    if Yes_No == 'Yes' or Yes_No == 'Y':
        calc()
    elif Yes_No == 'No' or Yes_No == 'N':
        print('Exit---')    
    else:
        print('Please enter the Yes or No') 
