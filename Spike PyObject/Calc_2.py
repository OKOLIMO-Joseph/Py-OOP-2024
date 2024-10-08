operator = input("Please enter the operator... :")
num1 = float(input("Enter th first number : "))
num2 = float(input("Enter the second number : "))

if operator == "+":
    result = num1 + num2
    print("Total = " +str(result))

elif operator == "-":
    result = num1 - num2
    print("Difference = "+str(result)) 

elif operator == "/":
    result = num1 / num2
    print("Quotient = "+str(result))

elif operator == "*":
    result = num1 * num2
    print("Product = " +str(result))


else:
    print("You entered an invalid operator!")