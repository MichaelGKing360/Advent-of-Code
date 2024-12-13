def main():
    print('Welcome to the Sum Calculator!')

    try:
        # Get user inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calc the sum
        sum = num1 + num2

        # Display the result
        print(f"The sume of {num1} and {num2} is {sum}!")

    except:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
