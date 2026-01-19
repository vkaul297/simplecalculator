# Simple Calculator

A command-line calculator application written in Python that supports basic arithmetic operations and calculation history.

## Features

### Implemented
- **Basic Operations**:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with zero-division error handling)
  - Power (exponentiation)
  - Square root (with negative number error handling)

- **Calculation History** ✨ (New Feature):
  - Automatically tracks all calculations
  - View complete calculation history
  - Clear history when needed
  - Persists during the session

### Future Enhancements (TODOs)
- Memory functions (M+, M-, MR, MC)
- Modulo operation
- Factorial operation
- Trigonometric functions (sin, cos, tan)
- Logarithm functions

## Usage

### Running the Calculator
```bash
python3 calculator.py
```

### Menu Options
```
=== Simple Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. View History
8. Clear History
0. Exit
========================
```

### Running Tests
```bash
python3 test_calculator.py
```

## Examples

### Basic Calculation
```
Enter your choice (0-8): 1
Enter first number: 15
Enter second number: 7
Result: 15.0 + 7.0 = 22.0
```

### Viewing History
```
Enter your choice (0-8): 7

=== Calculation History ===
1. 15.0 + 7.0 = 22.0
2. 100.0 - 45.0 = 55.0
3. 8.0 × 7.0 = 56.0
===========================
```

## Requirements
- Python 3.6 or higher
- No external dependencies required

## License
MIT License
