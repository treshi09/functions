#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def add(a, b):
    print("The sum is:", a + b)

def subtract(a, b):
    print("The difference is:", a - b)

def divide(a, b):
    print("The quotient is:", a / b)

def multiply(a, b):
    print("The multiplication is:", a * b)

print("a. Add")
print("b. Subtract")
print("c. Divide")
print("d. Multiply")
choice = input("Enter your choice: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if choice == 'a':
    add(num1, num2)
elif choice == 'b':
    subtract(num1, num2)
elif choice == 'c':
    divide(num1, num2)
elif choice == 'd':
    multiply(num1, num2)