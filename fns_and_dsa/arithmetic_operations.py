def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1/num2
    else:
        return "Error: Invalid operation"
from calculator import perform_operation

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_operation():
    operations = ['add', 'subtract', 'multiply', 'divide']
    while True:
        op = input("Enter operation (add, subtract, multiply, divide): ").lower()
        if op in operations:
            return op
        print("Invalid operation. Please choose from: add, subtract, multiply,divide.")
def main():
    print("Welcome to the calculator!")
    num1 = get_float("Enter the first number: ")
    num2 = get_float("Enter the first number: ")
    operation = get_operation()
    result = perform_operation(num1, num2, operation)
    if isinstance(result, str) and result.startswith("Error"):
        print(result)
    else:
        print(f"Result: {result}")
if __name__== "__main__"
    main()
    



