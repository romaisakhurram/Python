def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message, end=" ") 

def main():

    message = input("\033[94m Please type a message: \033[0m")

    repeats = int(input("\033[94m Enter a number of times to repeat your message: \033[0m"))

    print_multiple(message, repeats)

if __name__ == "__main__":
    main()