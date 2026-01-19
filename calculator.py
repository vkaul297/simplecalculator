#!/usr/bin/env python3
"""
PokéCalc - Pokemon-Themed Calculator
A wild calculator appears! Use math moves to battle numbers!
"""

import math
import sys
import random

class PokeCalculator:
    def __init__(self):
        self.result = 0
        self.battle_log = []
        self.trainer_name = "Ash"
        # TODO: Add memory functions (Rare Candy storage)

    def add(self, a, b):
        """Pikachu used Thunder Shock! Numbers combine!"""
        return a + b

    def subtract(self, a, b):
        """Charmander used Ember! Numbers shrink!"""
        return a - b

    def multiply(self, a, b):
        """Mewtwo used Psychic! Numbers multiply!"""
        return a * b

    def divide(self, a, b):
        """Squirtle used Water Gun! Numbers divide!"""
        if b == 0:
            raise ValueError("Oh no! You can't divide by zero! It's super ineffective!")
        return a / b

    def power(self, a, b):
        """Charizard used Fire Blast! MEGA POWER!"""
        return a ** b

    def sqrt(self, a):
        """Eevee used Swift! Finding square root!"""
        if a < 0:
            raise ValueError("Eevee can't calculate square root of negative numbers! It fainted!")
        return math.sqrt(a)

    def add_to_battle_log(self, calculation):
        """Record the battle in your Trainer Journal"""
        self.battle_log.append(calculation)

    def view_battle_log(self):
        """Check your Trainer Journal - see all your math battles!"""
        if not self.battle_log:
            print("\n🎮 Your Trainer Journal is empty! No battles yet, Trainer!")
            return

        print("\n" + "="*50)
        print("📖 TRAINER JOURNAL - BATTLE LOG 📖")
        print("="*50)
        for i, calc in enumerate(self.battle_log, 1):
            print(f"Battle #{i}: {calc}")
        print("="*50)

    def clear_battle_log(self):
        """Use a Pokémon Center to clear your battle log!"""
        self.battle_log = []
        print("\n🏥 Nurse Joy: 'Your Trainer Journal has been refreshed! Good luck on your journey!'")

    # TODO: Add modulo operation (Ditto Transform!)
    # TODO: Add factorial operation (Magikarp Evolution!)
    # TODO: Add trigonometric functions (Legendary Bird Trio!)
    # TODO: Add logarithm functions (Professor Oak's Research!)

def print_poke_menu():
    """Display the PokéCalc battle menu!"""
    print("\n" + "="*50)
    print("⚡ POKÉCALC - CHOOSE YOUR MATH MOVE! ⚡")
    print("="*50)
    print("1. ⚡ Thunder Shock (Add) - Pikachu")
    print("2. 🔥 Ember (Subtract) - Charmander")
    print("3. 🧠 Psychic (Multiply) - Mewtwo")
    print("4. 💧 Water Gun (Divide) - Squirtle")
    print("5. 🔥 Fire Blast (Power) - Charizard")
    print("6. ⭐ Swift (Square Root) - Eevee")
    print("7. 📖 Trainer Journal (View Battle Log)")
    print("8. 🏥 Pokémon Center (Clear Battle Log)")
    print("0. 🚪 Return to Pallet Town (Exit)")
    print("="*50)

def get_number(prompt):
    """Catch a wild number!"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  The wild number fled! Please enter a valid number, Trainer!")

def print_pokemon_intro():
    """Show the Pokemon intro!"""
    print("\n" + "="*50)
    print("🎮 WELCOME TO POKÉCALC! 🎮")
    print("="*50)
    print("Professor Oak: 'Welcome to the world of Pokémon'")
    print("              'and mathematics!'")
    print("\n🎒 Trainer, choose your math moves wisely!")
    print("="*50)

def main():
    """Main PokéCalc adventure loop!"""
    calc = PokeCalculator()
    print_pokemon_intro()

    while True:
        print_poke_menu()
        choice = input("\n🎯 What will you do? (0-8): ")

        if choice == '0':
            print("\n" + "="*50)
            print("👋 Professor Oak: 'Safe travels, Trainer!'")
            print("   'May your calculations be ever accurate!'")
            print("="*50)
            sys.exit(0)

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("🎯 Catch the first number: ")
            num2 = get_number("🎯 Catch the second number: ")

            try:
                if choice == '1':
                    print("⚡ Pikachu is preparing Thunder Shock...")
                    result = calc.add(num1, num2)
                    calc_str = f"{num1} + {num2} = {result}"
                    print(f"✨ It's super effective! Result: {calc_str}")
                    calc.add_to_battle_log(calc_str)
                elif choice == '2':
                    print("🔥 Charmander is preparing Ember...")
                    result = calc.subtract(num1, num2)
                    calc_str = f"{num1} - {num2} = {result}"
                    print(f"✨ It's super effective! Result: {calc_str}")
                    calc.add_to_battle_log(calc_str)
                elif choice == '3':
                    print("🧠 Mewtwo is preparing Psychic...")
                    result = calc.multiply(num1, num2)
                    calc_str = f"{num1} × {num2} = {result}"
                    print(f"✨ It's super effective! Result: {calc_str}")
                    calc.add_to_battle_log(calc_str)
                elif choice == '4':
                    print("💧 Squirtle is preparing Water Gun...")
                    result = calc.divide(num1, num2)
                    calc_str = f"{num1} ÷ {num2} = {result}"
                    print(f"✨ It's super effective! Result: {calc_str}")
                    calc.add_to_battle_log(calc_str)
                elif choice == '5':
                    print("🔥 Charizard is preparing Fire Blast...")
                    result = calc.power(num1, num2)
                    calc_str = f"{num1} ^ {num2} = {result}"
                    print(f"🔥 CRITICAL HIT! Result: {calc_str}")
                    calc.add_to_battle_log(calc_str)
            except ValueError as e:
                print(f"💥 Attack failed! {e}")

        elif choice == '6':
            num = get_number("🎯 Catch a number: ")
            try:
                print("⭐ Eevee is preparing Swift...")
                result = calc.sqrt(num)
                calc_str = f"√{num} = {result}"
                print(f"✨ It's super effective! Result: {calc_str}")
                calc.add_to_battle_log(calc_str)
            except ValueError as e:
                print(f"💥 Attack failed! {e}")

        elif choice == '7':
            calc.view_battle_log()

        elif choice == '8':
            calc.clear_battle_log()

        else:
            print("❌ That's not a valid move! Choose again, Trainer!")

if __name__ == "__main__":
    main()
