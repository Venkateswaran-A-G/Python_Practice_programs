#Use map() and lambda to convert a list of Celsius temps to Fahrenheit.
cel = input("Enter celsius temperature list seperated by spaces: ")
converted = list(map(lambda x: (float(x) * 9/5) + 32, cel.split()))
print("Fahrenheit temperatures:", converted)