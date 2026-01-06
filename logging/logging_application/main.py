import os
from config.logging_config import setup_logger
from utils.calculator import divide
from utils.file_reader import read_number_from_file

logger = setup_logger()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NUMBER_FILE = os.path.join(BASE_DIR, "number.txt")

def main():
    logger.info("Application started")

    try:
        a = int(input("Enter first number: "))
        b = read_number_from_file(NUMBER_FILE, logger)

        result = divide(a, b, logger)
        print("Result:", result)

    except Exception:
        logger.critical("Application crashed", exc_info=True)
        print("Something went wrong. Check logs.")

    finally:
        logger.info("Application finished")

if __name__ == "__main__":
    main()
