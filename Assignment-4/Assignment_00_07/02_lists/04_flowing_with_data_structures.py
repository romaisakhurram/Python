def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    message = input("\033[1;3m Enter a message to copy: \033[0m ")

    my_list = []

    print("List before:", my_list)

    add_three_copies(my_list, message)

    print("List after:", my_list)

if __name__ == "__main__":
    main()