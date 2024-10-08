operator = input("Enter the operator you want to use : ")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number :"))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

else:
        print("You entered an invalid operator!")