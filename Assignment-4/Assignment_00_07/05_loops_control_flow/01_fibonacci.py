MAX_TERM_VALUE = 10000

def main():
    curr_term = 0  
    next_term = 1 
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

if __name__ == '__main__':
    main()