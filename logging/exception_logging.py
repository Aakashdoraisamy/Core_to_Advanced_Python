import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)

except Exception:
    logging.exception("Exception occurred")
    print("Error occurred")
