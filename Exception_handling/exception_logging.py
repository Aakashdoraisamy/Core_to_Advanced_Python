import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("Program started")

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
        print("Result:", result)

    except ZeroDivisionError as e:
        logging.error("Division by zero", exc_info=True)
        print("Cannot divide by zero")

    except ValueError as e:
        logging.error("Invalid input", exc_info=True)
        print("Enter valid numbers")

except Exception as e:
    logging.critical("Unexpected error occurred", exc_info=True)
    print("Something went wrong")

finally:
    print("Program ended")
