#!/usr/bin/env python3
"""
Test script for the Simple Calculator
"""

from calculator import Calculator

def test_calculator():
    """Test calculator operations and history feature"""
    calc = Calculator()

    print("Testing calculator operations...")

    # Test addition
    result = calc.add(5, 3)
    assert result == 8, "Addition test failed"
    calc.add_to_history(f"5 + 3 = {result}")
    print(f"✓ Addition: 5 + 3 = {result}")

    # Test subtraction
    result = calc.subtract(10, 4)
    assert result == 6, "Subtraction test failed"
    calc.add_to_history(f"10 - 4 = {result}")
    print(f"✓ Subtraction: 10 - 4 = {result}")

    # Test multiplication
    result = calc.multiply(7, 6)
    assert result == 42, "Multiplication test failed"
    calc.add_to_history(f"7 × 6 = {result}")
    print(f"✓ Multiplication: 7 × 6 = {result}")

    # Test division
    result = calc.divide(20, 4)
    assert result == 5, "Division test failed"
    calc.add_to_history(f"20 ÷ 4 = {result}")
    print(f"✓ Division: 20 ÷ 4 = {result}")

    # Test power
    result = calc.power(2, 8)
    assert result == 256, "Power test failed"
    calc.add_to_history(f"2 ^ 8 = {result}")
    print(f"✓ Power: 2 ^ 8 = {result}")

    # Test square root
    result = calc.sqrt(16)
    assert result == 4, "Square root test failed"
    calc.add_to_history(f"√16 = {result}")
    print(f"✓ Square Root: √16 = {result}")

    # Test division by zero
    try:
        calc.divide(10, 0)
        assert False, "Division by zero should raise ValueError"
    except ValueError:
        print("✓ Division by zero error handling works")

    # Test negative square root
    try:
        calc.sqrt(-4)
        assert False, "Negative square root should raise ValueError"
    except ValueError:
        print("✓ Negative square root error handling works")

    # Test history feature
    print("\nTesting history feature...")
    print(f"✓ History contains {len(calc.history)} calculations")
    assert len(calc.history) == 6, "History should contain 6 calculations"

    # View history
    calc.view_history()

    # Clear history
    calc.clear_history()
    assert len(calc.history) == 0, "History should be empty after clearing"
    print("✓ History cleared successfully")

    # Test empty history
    print("\nTesting empty history view:")
    calc.view_history()

    print("\n✓ All tests passed!")

if __name__ == "__main__":
    test_calculator()
