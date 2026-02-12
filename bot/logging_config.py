import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(log_file="trading_bot.log"):
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_formatter = logging.Formatter(
        "%(levelname)s: %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=2
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.WARNING)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
