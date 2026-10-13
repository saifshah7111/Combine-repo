def temp():
    Temperature = int(input("Enter Temperature: "))
    Unit = str(input("°C or °F: ")).title()
    if Unit == 'C' or Unit == '°C':
        print('Temperature in Fahrenheit = ',round(Temperature * 1.8 + 32,2),'°F')
    elif Unit == 'F' or Unit == '°F':
        print('Temperature in Celsius = ',round((Temperature - 32) / 1.8,2),'°C')
    else:
        print('Please enter the following units') 
temp()   
yn = ""     
while yn != "No" and yn != "N":
    print("-----------------------------")
    yn = str(input("Want to continue? : ")).title()
    print("-----------------------------")
    if yn == "Yes" or yn == "Y":
        temp()
    elif yn == "No" or yn == "N":   
        print("Exit-") 
    else:
        print("Please enter Yes or No")    
       
    
    
