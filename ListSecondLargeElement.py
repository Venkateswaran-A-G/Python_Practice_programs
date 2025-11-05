#Write a program to find the second largest element in a list.
s1 = input("Enter the elements of the list separated by space: ")
lst = list(map(int, s1.split()))
max = max(lst)
lst.remove(max)
second_max = max(lst)
print("The second largest element in the list is:", second_max)

