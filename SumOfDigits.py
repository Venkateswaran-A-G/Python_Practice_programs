#Sum of digits of a given number.
n = input("Enter a number: ")
sum = 0
for i in n:
    sum = sum + int(i)
print(sum)