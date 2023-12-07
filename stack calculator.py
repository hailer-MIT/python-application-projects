class Calculator:
    def __init__(self):
        self.stack = []

    def push(self, num1, num2):
        self.stack.append(num1)
        self.stack.append(num2)

    def add(self):
        if len(self.stack) >= 2:
            num2 = self.stack.pop()
            num1 = self.stack.pop()
            self.stack.append(num1 + num2)
        else :
            print("\n\nERROR!!!\nfirst enter2 numbers youwant to calculate\n\n")
    def subtract(self):
        if len(self.stack) >= 2:
            num2 = self.stack.pop()
            num1 = self.stack.pop()
            self.stack.append(num1 - num2)
        else :
            print("\n\nERROR!!!\nfirst enter2 numbers youwant to calculate\n\n")
    def multiply(self):
        if len(self.stack) >= 2:
            num2 = self.stack.pop()
            num1 = self.stack.pop()
            self.stack.append(num1 * num2)
        else: 
            print("\n\nERROR!!!\nfirst enter2 numbers youwant to calculate\n\n")
    def divide(self):
        if len(self.stack) >= 2:
            num2 = self.stack.pop()
            num1 = self.stack.pop()
            self.stack.append(num1 / num2)
        else:
            print("\n\nERROR!!!\nfirst enter2 numbers youwant to calculate\n\n")
    def get_result(self):
        return self.stack[-1] if self.stack else None


# Create a Calculator object
calculator = Calculator()

# User interaction loop
while True:
    print("Calculator Menu:")
    print("1. enter two numbers")
    print("2. Add")
    print("3. Subtract")
    print("4. Multiply")
    print("5. Divide")
    print("6. Get Result")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter second number:"))
        calculator.push(num1, num2)
    elif choice == '2':
        calculator.add()
    elif choice == '3':
        calculator.subtract()
    elif choice == '4':
        calculator.multiply()
    elif choice == '5':
        calculator.divide()
    elif choice == '6':
        result = calculator.get_result()
        if result is not None:
            print("Result: ", result)
        else:
            print("Stack is empty.")
    elif choice == '0':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice. Please try again.")