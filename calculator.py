#!/usr/bin/env python3
"""
Simple Calculator Application
Supports basic arithmetic operations
"""

import math
import sys

class Calculator:
    def __init__(self):
        self.result = 0
        self.history = []
        # TODO: Add memory functions (M+, M-, MR, MC)

    def add(self, a, b):
        """Add two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Raise a to the power of b"""
        return a ** b

    def sqrt(self, a):
        """Calculate square root of a"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)

    def add_to_history(self, calculation):
        """Add a calculation to history"""
        self.history.append(calculation)

    def view_history(self):
        """Display calculation history"""
        if not self.history:
            print("\nNo calculations in history.")
            return

        print("\n=== Calculation History ===")
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
        print("===========================")

    def clear_history(self):
        """Clear all calculation history"""
        self.history = []
        print("\nHistory cleared.")

    # TODO: Add modulo operation
    # TODO: Add factorial operation
    # TODO: Add trigonometric functions (sin, cos, tan)
    # TODO: Add logarithm functions

def print_menu():
    """Display calculator menu"""
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. View History")
    print("8. Clear History")
    print("0. Exit")
    print("========================")

def get_number(prompt):
    """Get a number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main calculator loop"""
    calc = Calculator()

    while True:
        print_menu()
        choice = input("Enter your choice (0-8): ")

        if choice == '0':
            print("Thank you for using Simple Calculator!")
            sys.exit(0)

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            try:
                if choice == '1':
                    result = calc.add(num1, num2)
                    calc_str = f"{num1} + {num2} = {result}"
                    print(f"Result: {calc_str}")
                    calc.add_to_history(calc_str)
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    calc_str = f"{num1} - {num2} = {result}"
                    print(f"Result: {calc_str}")
                    calc.add_to_history(calc_str)
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    calc_str = f"{num1} × {num2} = {result}"
                    print(f"Result: {calc_str}")
                    calc.add_to_history(calc_str)
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    calc_str = f"{num1} ÷ {num2} = {result}"
                    print(f"Result: {calc_str}")
                    calc.add_to_history(calc_str)
                elif choice == '5':
                    result = calc.power(num1, num2)
                    calc_str = f"{num1} ^ {num2} = {result}"
                    print(f"Result: {calc_str}")
                    calc.add_to_history(calc_str)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '6':
            num = get_number("Enter number: ")
            try:
                result = calc.sqrt(num)
                calc_str = f"√{num} = {result}"
                print(f"Result: {calc_str}")
                calc.add_to_history(calc_str)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '7':
            calc.view_history()

        elif choice == '8':
            calc.clear_history()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
