def con():
    weight = int(input('Weight: '))
    unit = str(input('(L)bs or (K)g: ')).title()
    if unit == "L" or unit == 'Lbs' :
        converted = weight * 0.45
        print("You are", round(converted,3), "kilos")
    elif unit == 'K' or unit == 'Kg':
        converted = weight / 0.45
        print("You are", round(converted,3), "pounds")
    else:
        print('Please type Kg or Lbs')    
con()
Yes_No = "" 
while Yes_No != "No" and Yes_No != "N":
    print('---------------')
    Yes_No = str(input('want to continue? : ')).title()
    if Yes_No == "Yes" or Yes_No == "Y":
        con()
    elif Yes_No == "No" or Yes_No == "N":   
        print('Exit--')
    else:
        print('Please type Yes or No')
    
