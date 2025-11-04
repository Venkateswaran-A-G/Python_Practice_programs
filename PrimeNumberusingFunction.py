#Write a function to check if a number is prime.
def isPrime(n):
    ran = int(n**(1/2))+1
    for i in range(2,ran):
        if n % i == 0:
            return False
    return True