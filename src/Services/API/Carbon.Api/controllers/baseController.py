from logging import Logger
from fastapi import Depends
from customLogging.logger import ILogger


class BaseController:
    _logger: Logger = Depends(ILogger)