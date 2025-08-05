# Division of two numbers
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
if b != 0:
    div_result = a / b
    print("Quotient:", div_result)
else:
    print("Error: Cannot divide by zero!")
