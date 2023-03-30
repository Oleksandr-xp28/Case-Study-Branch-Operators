if __name__ == '__main__':
    try:
        begin = int(input('Enter a begin: ')) 
        end = int(input('Enter an end: ')) 
        max = min = begin
        for i in range(begin, end+1):
            if i > max:
                max = i
            if i < min:
                min = i
        print(f"The maximum number is: {max}")
    except :
        print("Invalid input")
        print("The number is not in range")