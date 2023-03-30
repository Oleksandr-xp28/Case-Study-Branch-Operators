if __name__ == '__main__':
    try:
        i = int(input("Enter a number: "))
        if i % 7 == 0:
            print("Number is multiple 7")
        elif i % 7 != 0:
            print("Number is not multiple 7")
        else:


        pass
    except:
        print("Invalid input")