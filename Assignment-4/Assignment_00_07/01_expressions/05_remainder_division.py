def main():
   
    dividend = int(input("\033[1;3m Please enter an integer to be divided: \033[0m "))

    divisor = int(input("\033[1;3m Please enter an integer to divide by: \033[0m "))

    quotient = dividend // divisor  

    remainder= dividend % divisor  
    
    print(f"The result of this division is {quotient}  with a remainder of {remainder}")

if __name__ == '__main__':
    main()
