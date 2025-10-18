#Find common elements in two lists.
l1 = input("Enter a list seperated by whitespaces: ").split()
l2 = input("Enter a list seperated by whitespaces: ").split()
print(l1)
print(l2)
print("Common elements are: ")
for i in l1:
    if i in l2:
        print(i)