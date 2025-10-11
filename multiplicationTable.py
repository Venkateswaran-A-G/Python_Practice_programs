#Print a multiplication table of a number given by user.
n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")