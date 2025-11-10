#Count how many even and odd numbers are in a given list.
l = input("Enter the list of number seperated by space: ").split()
ec,oc =0,0
for num in l:
    if int(num)%2==0:
        ec+=1
    else:
        oc+=1
print("Even count:",ec) 
print("Odd count:",oc)
