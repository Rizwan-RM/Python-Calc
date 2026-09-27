operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(num1 + num2)

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)          
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print(f"Invalid operator: {operator}. is not valid")
