def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def main ():
    print("Simple Calculator")
    print("Choose an operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        print("invalid input. Please enter 1, 2, 3 or 4.")
    
    while True:
            try:
                 num1 = float(input("Enter first number: "))
                 num2 = float(input("Enter second number: "))
                 break
            except ValueError:
                 print("Invalid number. Please enter valid numeric values.")

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
         print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
         print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
         print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
     main()