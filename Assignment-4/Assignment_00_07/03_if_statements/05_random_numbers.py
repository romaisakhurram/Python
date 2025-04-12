import random

N_NUMBERS  = 10
MIN_VALUE  = 1
MAX_VALUE  = 100

def main():

    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print("Random numbers:", random_numbers)
    
    total_sum = sum(random_numbers)
    
if __name__ == '__main__':
    main()