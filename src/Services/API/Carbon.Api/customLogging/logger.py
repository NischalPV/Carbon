import logging.config
from os import path
from typing import Any
import logging


class Logger:
    logger: logging.Logger
    name: str = __name__

    def __init__(self) -> None:
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
        logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
        self.logger = logging.getLogger(self.name)
        self.logger.info("Logger initialized!")


_logger = Logger()


async def ILogger() -> Logger:
    # _logger.name = name
    return _logger.logger 
