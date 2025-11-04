#Write a function to calculate the Fibonacci sequence up to N terms.
def fibonacci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def seq(n):
    for i  in range(n):
        print(fibonacci(i))
