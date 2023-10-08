#!/usr/bin/python3
def add_integer(a, b=98):
    """
    >>> add_integer(2, 3)
    5
    """
    try :
        isinstance(a, (int, float))
        if isinstance(a, float):
            a = int(a)
    except TypeError:
        print("a must be an integer")
    try :
        isinstance(b, (int, float))
        if isinstance(b, float):
            b = int(b)
    except TypeError:
        print("b must be an integer")
    return a + b
        
        
    
