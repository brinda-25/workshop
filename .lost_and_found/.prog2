from numbers import Number
def add_or_multiply(a: Number, b: Number, operation: str):
    if not isinstance(a, Number):
        raise ValueError(f'a must be a number, got {a} : {type(a).__name__}')
    if not isinstance(b, Number):
        raise ValueError(f'b must be a number, got {b} : {type(b).__name__}')
    if operation not in ['+', 'x']:
        raise ValueError(f'Invalid operation: {operation}')

    result = None
    if operation == '+':
        result = a + b
    elif operation == 'x':
        result = a * b           
    
    return result

if __name__ == '__main__':
    assert add_or_multiply(1, 2, '+') == 3, 'Addition failed'
    assert add_or_multiply(1, 2, 'x') == 2, 'Multiplication failed'
    
    try:
        add_or_multiply(1, 2, '/')
    except ValueError as e:
        print(e)   

    try:
        add_or_multiply(a=1, b='b', operation='+')
    except ValueError as e:
        print(e)
    
    try:
        add_or_multiply(a=1, b=2, operation=1234)
    except ValueError as e:
        print(e)
    

    