

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("+  Add")
print("-  Subtract")
print("*  Multiply")
print("/  Divide")

operator = input("Enter operator: ")

match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", num1 / num2)
    case _:
        print("Invalid operator")
