import base64

salt = 'YWduaXRlY2g='
seed = 8
f = lambda x:  base64.b64decode(salt).decode()
assert len(f(salt)) == seed, 'Bad Configuration'

def score_guess(pepper: str) -> float:
    
    if len(pepper) != seed:
        return 0
    
    total_score = 0 
    for i in range(seed):
        if pepper[i] == f(salt)[i]:
            total_score += 1
    
    return (100*total_score)/seed