# Code Snippets.  
# Logging and Type Hinting. 
import logging

def add_ints(x: int,y: int) -> int:
    """ Add two numbers. """
    return x+y

if __name__ == "__main__":
    x = 10
    y = 25
    sum = add_ints(x,y)
    result = "When {} and {} are added, result is: {}".format(x,y,sum)
    logging.debug(result)
