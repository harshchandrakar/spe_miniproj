import math

class ScientificCalculator:
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return math.sqrt(x)

    def factorial(self, x):
        if x < 0:
            raise ValueError("Cannot compute factorial of a negative number.")
        return math.factorial(x)

    def natural_log(self, x):
        if x <= 0:
            raise ValueError("Cannot compute natural logarithm of non-positive numbers.")
        return math.log(x)

    def power(self, x, b):
        return math.pow(x, b)

if __name__ == "__main__":
    calculator = ScientificCalculator()
    while True:
        print("\nScientific Calculator")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")
        
        if choice == '1':
            x = float(input("Enter a number: "))
            try:
                print("Result:", calculator.square_root(x))
            except ValueError as e:
                print("Error:", e)
        elif choice == '2':
            x = int(input("Enter a number: "))
            try:
                print("Result:", calculator.factorial(x))
            except ValueError as e:
                print("Error:", e)
        elif choice == '3':
            x = float(input("Enter a number: "))
            try:
                print("Result:", calculator.natural_log(x))
            except ValueError as e:
                print("Error:", e)
        elif choice == '4':
            x = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", calculator.power(x, b))
        elif choice == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice. Please try again.")
