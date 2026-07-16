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