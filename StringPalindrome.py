#Check if a string is a palindrome.
string = input("Enter a String: ")
if(string == string[::-1]):
    print("Palindrome")
else:
    print("Not a Palindrome")