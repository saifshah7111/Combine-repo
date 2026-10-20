def bmi():
    Weight = int(input('Enter weight in kg = '))
    Height = int(input('Enter height in meters = '))
    print('BMI index = ', round(Weight / Height ** 2,2))
bmi()
yn = ''
while yn != 'No' and yn != 'N':
    print('---------------------------')
    yn = str(input('Want to continue? - ')).title()
    print('---------------------------')
    if yn == 'Yes' or yn == 'Y':
        bmi()
    elif yn == 'No' or yn == 'N':   
        print('Exit-')  
    else:
        print('Please enter yes or no')
