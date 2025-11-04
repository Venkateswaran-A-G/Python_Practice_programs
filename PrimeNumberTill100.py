#Print all prime numbers between 1 and 100.
def prime(n):
    for i in range(2,(n//2)+1):
        if (n%i == 0):
            return 0
    return 1
for i in range(1,101):
    j = prime(i)
    if(j == 1):
        print(i,end=" ")