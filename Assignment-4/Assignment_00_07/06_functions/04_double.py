def double(num: int):
    return num * 2

def main():
    num = int(input("\033[1;3m Enter a number: \033[0m"))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()