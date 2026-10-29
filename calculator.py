
# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

op = input("Enter your choice: ")

if op == "+":
    result = num1 + num2
    print("Result:", result)

elif op == "-":
    result = num1 - num2
    print("Result:", result)

elif op == "*":
    result = num1 * num2
    print("Result:", result)

elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation!")
