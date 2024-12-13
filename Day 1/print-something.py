def main():
    print('Welcome to the Sum Calculator!')

    try:
        # Get user inputs
        string1 = input("Enter the first phrase: ")
        string2 = input("Enter the second phrase: ")

        # Display the result
        print(f"{string1}!")
        print(f"{string2}!")

    except:
        print("Invalid input. Please enter alphanumeric phrase values.")

if __name__ == "__main__":
    main()
