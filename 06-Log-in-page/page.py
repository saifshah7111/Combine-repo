print ('Type Create Account (to create an account)')
print ('Type Log In (to log in)')
Account = input("Create Account Or Log In - ").lower().upper().title()
Create_Password = " "
Password = " "
if Account == ('Create Account'):
    Name = str(input('Enter Name - ')).title()
    Username = input('Username - ')
    print('Date_of_Birth: ')
    Date = (input('Date - '))
    Month = (input('Month - '))
    Year = int(input('Year - '))
    Gender = str(input('Gender - ')).lower().upper().title()
    if Gender == 'Male' or 'M':
        Email = input('Enter Email address - ').lower()
        Create_Password = input('Create Password - ')
        Password = " "
    elif Gender == 'Female' or 'F':    
        Email = input('Enter Email address - ').lower()
        Create_Password = input('Create Password - ')
        Password = " "
    else:
        print('please type your gender')    
    while Password != Create_Password:
        Password = input('Enter Password - ')
        if Password == Create_Password:
            print('------------')
            print('Name - ' + Name)
            print('Username - ' + Username)
            print('Date of Birth - ' + str(Date) + '-' + str(Month) + '-' + str(Year))
            if Gender == 'M' or 'Male':
                print('Gender - Male')
            elif Gender == 'F' or 'Female':
                print('Gender - Female')    
            print('Email - ' + Email)
            print('Password - ' + Password)
            print('Your account succesfully created')
        else:
            print('Password Incorrect')
    print('------------')        
    print("want to log in?")  
    Yes_No = str(input('Type Yes or No - ')).lower().upper().title()  
    
    if Yes_No == 'Yes': 
        Username1 = ""
        Password1 = ""
        trys = 0
        try_count = 3
        while Password != Password1 and Username != Username1 and trys != try_count:
            Username1 = input('Username - ')
            Password1 = input('Enter Password - ')
            if Username == Username1 and Password == Password1 and trys != try_count:
                print('Username and Password are correct')
                print('Access Granted')
            else:
                print('Username and Password are Incorrect')
                print('Access Denied')   
                trys += 1
                if trys == try_count:
                    print("")
                    print("Too many attempts, Try again later")
    elif Yes_No == 'No': 
        print('Quit') 
    else:
        print('please type Yes or No')               
elif Account == ('Log In'):
    Username = ""
    Password = ""
    trys2 = 0
    try_count2 = 3
    while Username != '1m' and Password != '2m' and trys2 != try_count2:
        Username = input('Enter Username - ')
        Password = input('Enter Password - ')
        if Username == '1m' and Password == '2m' and trys2 != try_count2:
            print('Username and Password are correct')
            print('Access Granted')
        else:
            print('Username and Password are Incorrect')
            print('Access Denied')   
            print('------------------------')
            trys2 += 1
            if trys2 == try_count2:
                print("Too many attempts, Try again later")
else: 
    print('please enter Create Account or Log In')
    

    
