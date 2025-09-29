FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    insert = float(input("Enter the temperature to convert: "))
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")


temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temp_type == "F":
    temp = convert_to_celsius(insert)
    print (f"{insert}\u00B0C is {temp}\u00B0C")
elif temp_type == "C":
    temp = convert_to_fahrenheit(insert)
    print (f"{insert}\u00B0F is {temp}\u00B0F")
