def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("=== Simple Calculator ===")
    print("Operations: add, subtract, multiply, divide")

    operation = input("Enter operation: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in ops:
        print(f"Unknown operation: {operation}")
        return

    try:
        result = ops[operation](a, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
