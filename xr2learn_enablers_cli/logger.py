import logging


def logging_function_exit_status(logger=None):
    if logger is None:
        logger = logging.getLogger("cli_logger")
        logger.setLevel(logging.INFO)

    def decorator(call_func):
        def wrapper(*args, **kwargs):
            logger.info("##################################################")
            logger.info(f"Start {call_func.__name__}")
            logger.info(f"Args: {args}")
            logger.info(f"Kwargs: {kwargs}")
            if call_func(*args, **kwargs):
                logger.info("OK: exit code 1")
            else:
                logger.error("Exit code 0")
            logger.info("##################################################")
        return wrapper
    return decorator
