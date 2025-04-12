def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("\033[94m Enter a number: \033[0m"))
    print_divisors(num)
    
if __name__ == '__main__':
    main()