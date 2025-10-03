#Sum of first N natural numbers.
n = int(input("Enter a positive integer: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    sum_n = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is {sum_n}")