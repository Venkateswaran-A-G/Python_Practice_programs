#Count the number of vowels in a string.
string = input("Enter a String: ")
c=0
for i in string:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        c+=1
print("Number of vowels: ",c)