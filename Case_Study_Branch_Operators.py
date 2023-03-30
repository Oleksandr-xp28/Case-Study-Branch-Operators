if __name__ == '__main__':
    try:
        i = int(input("Enter a number: "))
        if i % 2 == 0:
            print("The number is even")
        elif i % 2 != 0:
            print("The number is odd")
        else:
            print("The number is not in range")
    except Exception:
        print("Invalid input")