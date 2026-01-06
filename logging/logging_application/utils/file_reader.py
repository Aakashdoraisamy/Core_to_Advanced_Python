def read_number_from_file(file_path, logger):
    logger.info(f"Reading file: {file_path}")

    try:
        with open(file_path, "r") as f:
            value = int(f.read().strip())
            logger.debug(f"Read value: {value}")
            return value

    except FileNotFoundError:
        logger.error("File not found", exc_info=True)
        raise

    except ValueError:
        logger.error("Invalid number in file", exc_info=True)
        raise
