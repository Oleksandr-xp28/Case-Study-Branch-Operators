if __name__ == '__main__':
    try:
        begin = int(input('Enter a begin: ')) 
        end = int(input('Enter an end: ')) 
        max = min = begin
        for i in range(begin, end):
            if i < min:
                min = i
            if i > max:
                max = i
        print('The minimum is', min)
    except :
        print("Invalid input")
        print("The number is not in range")