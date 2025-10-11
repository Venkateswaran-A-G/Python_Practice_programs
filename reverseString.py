#Reverse a string without using slicing ([::-1]).
string = input("Enter a String: ")
length = len(string)
string2 = ""
for i in range(-1,-(length+1),-1):
    string2 = string2 + string[i]
print("Original String: ",string)
print("String after reversing: ",string2)