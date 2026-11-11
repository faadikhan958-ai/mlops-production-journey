
import logging
import sys

def setup_logger():
    logger = logging.getLogger("ml_api")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
          "%(asctime)s | %(levelname)s | %(module)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # INFO and WARNING -> stdout
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.INFO)
        stdout_handler.addFilter(
            lambda record: record.levelno < logging.ERROR
        )
        stdout_handler.setFormatter(formatter)

        # ERROR and CRITICAL -> stderr
        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setLevel(logging.ERROR)
        stderr_handler.setFormatter(formatter)

        logger.addHandler(stdout_handler)
        logger.addHandler(stderr_handler)

    return logger

logger = setup_logger()
