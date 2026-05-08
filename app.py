def main():
    print("=================================")
    print("   Welcome to My Python App 🚀   ")
    print("=================================")

    name = input("Enter your name: ")
    print(f"Hello {name}, welcome to DevOps learning!")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\nResults:")
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")

    if b != 0:
        print(f"Division: {a / b}")
    else:
        print("Division: Not possible (divide by zero)")

if __name__ == "__main__":
    main()
