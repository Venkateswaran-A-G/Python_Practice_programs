print("___Temperature Conversion___")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")
while True:
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == 3:
        break
    else:
        print("Invalid choice! Please select either 1,2 or 3.")