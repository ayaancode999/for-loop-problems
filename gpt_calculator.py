import math

def scientific_calculator():
    print("=== Scientific Calculator ===")
    print("""
Operations:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Power (x^y)
6. Square Root (√x)
7. Sine (sin x)
8. Cosine (cos x)
9. Tangent (tan x)
10. Log base 10 (log x)
11. Natural Log (ln x)
12. Factorial (x!)
13. Exit
""")

    while True:
        choice = input("Choose an operation (1–13): ")

        if choice == "13":
            print("Calculator closed.")
            break

        try:
            if choice in {"1", "2", "3", "4", "5"}:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", x + y)
                elif choice == "2":
                    print("Result:", x - y)
                elif choice == "3":
                    print("Result:", x * y)
                elif choice == "4":
                    print("Result:", "Error" if y == 0 else x / y)
                elif choice == "5":
                    print("Result:", math.pow(x, y))

            elif choice in {"6", "7", "8", "9", "10", "11", "12"}:
                x = float(input("Enter number: "))

                if choice == "6":
                    print("Result:", math.sqrt(x))
                elif choice == "7":
                    print("Result:", math.sin(math.radians(x)))
                elif choice == "8":
                    print("Result:", math.cos(math.radians(x)))
                elif choice == "9":
                    print("Result:", math.tan(math.radians(x)))
                elif choice == "10":
                    print("Result:", math.log10(x))
                elif choice == "11":
                    print("Result:", math.log(x))
                elif choice == "12":
                    print("Result:", math.factorial(int(x)))

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input. Try again.")
        except Exception as e:
            print("Error:", e)

        print()


if __name__ == "__main__":
    scientific_calculator()
