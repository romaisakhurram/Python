def main():

    side_1 = float(input("\033[1;3m Enter the length of side 1: \033[0m"))
    side_2 = float(input("\033[1;3m Enter the length of side 2: \033[0m"))
    side_3 = float(input("\033[1;3m Enter the length of side 3: \033[0m")) 

    print(f"The perimeter of the triangle is: {side_1 + side_2 + side_3}")

if __name__ == "__main__":
    main()