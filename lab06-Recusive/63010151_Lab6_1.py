num = int(input("Enter Number : "))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"{num}! = {factorial(num)}")