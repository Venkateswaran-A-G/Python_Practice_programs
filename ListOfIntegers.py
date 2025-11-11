#Given a list of integers, remove all elements less than 10.
integer = input("Enter the elements of the list seperated by space: ").split()
integer1 = [int(i) for i in integer if int(i)>10]
print(integer1)
