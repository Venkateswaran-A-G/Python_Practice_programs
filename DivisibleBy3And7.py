#Find all numbers between 1 and 1000 that are divisible by both 3 and 7.
def check_divisibility(n):
    if n%3==0:
        if(n%7==0):
            return True
def main():
    for i in range(1,1001):
        if check_divisibility(i):
            print(i,end=" ")
main()