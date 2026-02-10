#USN:1RUA25BCA0017 Name:Chandana H
#Factorail using recursion
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)

