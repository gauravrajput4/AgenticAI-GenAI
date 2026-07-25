import logging

# Basic loggin configure

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmaticApp")

def add(x, y):
    result= x + y
    logger.debug(f"result: {x}+{y}={result}")
    return result
def subtract(x, y):
    result= x - y
    logger.debug(f"result: {x}-{y}={result}")
    return result
def multiply(x, y):
    result= x * y
    logger.debug(f"result: {x}*{y}={result}")
    return result
def divide(x, y):
    try:
        result = x / y
        logger.debug(f"result: {x}/{y}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero")

add(10,15)
subtract(15,10)
multiply(10,15)
divide(10,0)
