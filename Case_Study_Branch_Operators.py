if __name__ == '__main__':
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        print("1 Addition")
        print("2 Subtraction")
        print("3 Multiplication")
        print("4 Arithmetic mean")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("The sum of the two numbers is:", num1 + num2)
        elif choice == 2:
            print("The difference of the two numbers is:", num1 - num2)
        elif choice == 3:
            print("The product of the two numbers is:", num1 * num2)
        elif choice == 4:
            sum = 0
            for i in range(num1, num2 + 1):
                sum += i
            mean = sum / (num2 - num1 + 1)
            print("The arithmetic mean of the two numbers is:", mean)
        else:
            print("Please enter a valid choice")
    except ValueError:
        print("Please enter a valid number")
