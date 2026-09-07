from fitness import score_guess
PASSWORD_LENGTH = 8
ALLOWED_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'

def guess_password():
    # write code to guess secret password (exacly 8 characters long, lowercase letters only) 
    # use score_guess() as many times to check if password is correct 
    # Scores range from 0 to 100 - Higher the score the better the guess
    #  return final password when score = 100
    return ''

if __name__ == '__main__':
    password = guess_password()
    print(f'The password is {password}')


## Hint 1 - Choose a random number from 0 to 7
##  import random
##  random_index = random.randint(0, PASSWORD_LENGTH-1)
##
## Hint 2 - Choose a random character from a-to-z
##  random_character = random.choice(ALLOWED_CHARACTERS)
##
## Hint 3 - Convert a string to a list
##  some_string = 'abcdefgh'
##  some_list = list(some_string)
##  print(some_list) --> outputs --> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',]
##
## Hint 4 - Merge a list of characters back into a string
##  some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',]
##  some_string = ''.join(some_list)
##  print(some_string) --> outputs --> 'abcdefgh'