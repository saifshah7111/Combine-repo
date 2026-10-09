Temperature = int(input("Enter Temperature: "))
Unit = str(input("°C or °F: ")).lower().upper()
if Unit == 'C' or Unit == '°C':
    print('Temperature in Fahrenheit = ',round(Temperature * 1.8 + 32,2),'°F')
elif Unit == 'F' or Unit == '°F':
    print('Temperature in Celsius = ',round((Temperature - 32) / 1.8,2),'°C')
else:
    print('Please enter the following units')    
       
    
