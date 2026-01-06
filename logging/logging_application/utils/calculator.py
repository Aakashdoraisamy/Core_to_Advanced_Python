def divide(a, b, logger):
    logger.info("Starting division operation")

    try:
        result = a / b
        logger.debug(f"Division result: {result}")
        return result

    except ZeroDivisionError:
        logger.error("Division by zero attempted", exc_info=True)
        raise
