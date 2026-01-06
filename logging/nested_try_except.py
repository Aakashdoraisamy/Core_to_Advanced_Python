import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    print("Outer try block")

    try:
        x = int(input("Enter number: "))
        y = int(input("Enter divisor: "))
        print(x / y)

    except ZeroDivisionError:
        logging.error("Division by zero", exc_info=True)
        print("Cannot divide by zero")

    except ValueError:
        logging.error("Invalid input", exc_info=True)
        print("Enter valid integers")

except Exception:
    logging.critical("Unexpected error", exc_info=True)

finally:
    print("Program finished")
