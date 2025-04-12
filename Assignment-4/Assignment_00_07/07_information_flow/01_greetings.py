def main():
    name : str = input("\033[1;3m What's your name? \033[0m")
    print(greet(name))

def greet(name):
    return "Greetings " + name + "!"
	
if __name__ == '__main__':
    main()
