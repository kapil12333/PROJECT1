def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def main():
    print("Welcome to the simple calculator!")
    
    while True:
        # Get the operation from the user
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
        
        if operation == 'exit':
            print("Goodbye!")
            break
        
        # Check if the operation is valid
        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation. Please enter one of +, -, *, /.")
            continue
        
        # Get numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        # Perform the operation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        # Print the result
        print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    main()

