import logging
from typing import Optional
from fletx.utils.context import AppContext

def get_logger(name: str) -> logging.Logger:
    """Gets a logger from the global context"""

    base_logger = AppContext.get_data("logger")
    if base_logger is None:

        # Fallback if the context is not initialized
        logger = logging.getLogger(name)
        logger.addHandler(logging.NullHandler())
        return logger
    return base_logger.getChild(name)