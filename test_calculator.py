#!/usr/bin/env python3
"""
Test script for the PokéCalc - Gotta test 'em all!
"""

from calculator import PokeCalculator

def test_calculator():
    """Test PokéCalc operations and battle log feature"""
    calc = PokeCalculator()

    print("🎮 Testing PokéCalc operations...")

    # Test addition
    result = calc.add(5, 3)
    assert result == 8, "Addition test failed"
    calc.add_to_battle_log(f"5 + 3 = {result}")
    print(f"⚡ Pikachu's Thunder Shock: 5 + 3 = {result}")

    # Test subtraction
    result = calc.subtract(10, 4)
    assert result == 6, "Subtraction test failed"
    calc.add_to_battle_log(f"10 - 4 = {result}")
    print(f"🔥 Charmander's Ember: 10 - 4 = {result}")

    # Test multiplication
    result = calc.multiply(7, 6)
    assert result == 42, "Multiplication test failed"
    calc.add_to_battle_log(f"7 × 6 = {result}")
    print(f"🧠 Mewtwo's Psychic: 7 × 6 = {result}")

    # Test division
    result = calc.divide(20, 4)
    assert result == 5, "Division test failed"
    calc.add_to_battle_log(f"20 ÷ 4 = {result}")
    print(f"💧 Squirtle's Water Gun: 20 ÷ 4 = {result}")

    # Test power
    result = calc.power(2, 8)
    assert result == 256, "Power test failed"
    calc.add_to_battle_log(f"2 ^ 8 = {result}")
    print(f"🔥 Charizard's Fire Blast: 2 ^ 8 = {result}")

    # Test square root
    result = calc.sqrt(16)
    assert result == 4, "Square root test failed"
    calc.add_to_battle_log(f"√16 = {result}")
    print(f"⭐ Eevee's Swift: √16 = {result}")

    # Test division by zero
    try:
        calc.divide(10, 0)
        assert False, "Division by zero should raise ValueError"
    except ValueError:
        print("💥 Division by zero error caught - It's super ineffective!")

    # Test negative square root
    try:
        calc.sqrt(-4)
        assert False, "Negative square root should raise ValueError"
    except ValueError:
        print("💥 Negative square root error caught - Eevee fainted!")

    # Test battle log feature
    print("\n📖 Testing Trainer Journal (Battle Log)...")
    print(f"✅ Battle Log contains {len(calc.battle_log)} math battles!")
    assert len(calc.battle_log) == 6, "Battle log should contain 6 calculations"

    # View battle log
    calc.view_battle_log()

    # Clear battle log
    calc.clear_battle_log()
    assert len(calc.battle_log) == 0, "Battle log should be empty after visiting Pokémon Center"
    print("✅ Battle Log cleared at Pokémon Center!")

    # Test empty battle log
    print("\n📖 Testing empty Trainer Journal:")
    calc.view_battle_log()

    print("\n🏆 All tests passed! You're a Pokémon Master of Math!")

if __name__ == "__main__":
    test_calculator()
