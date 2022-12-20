import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(filename)s:%(funcName)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('example_logging_module.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def substract_ints(x: int = 0,y: int = 0) -> int:
    """ Substract's two numbers. """
    return x-y

# if __name__ == "__main__":
x = 10
y = 6
ans = substract_ints(x,y)
result = "When {} and {} are substracted, result is: {}".format(x,y,ans)
logger.info(result)