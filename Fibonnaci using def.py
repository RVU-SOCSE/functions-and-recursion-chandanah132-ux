#USN:1RUA25BCA0017 Name:Chandana H
#Fibonnaci using def
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = 10
print("Fibonacci series:")
fibonacci(num)
