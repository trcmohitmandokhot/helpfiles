# Code Snippets.  
# Logging and Type Hinting. 
import sys
import logging

# Import Module
import example_logging_module

# Change root logger's configurations
logging.basicConfig(filename='example_logging.log',level=logging.DEBUG, 
                    format='%(asctime)s:%(filename)s:%(funcName)s:%(name)s:%(levelname)s:%(message)s')

def add_ints(x: int = 0,y: int = 0) -> int:
    """ Add two numbers. """
    return x+y

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    sum = add_ints(x,y)
    result = "When {} and {} are added, result is: {}".format(x,y,sum)
    logging.debug(result)
