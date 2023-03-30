if __name__ == '__main__':
    try:
        i = int(input("Enter a number: "))
        if i % 7 == 0:
            print("Number is multiple 7")
        elif i % 7 != 0:
            print("Number is not multiple 7")
        else:
            print("The number is not in range")
        pass
    except:
        print("Invalid input")