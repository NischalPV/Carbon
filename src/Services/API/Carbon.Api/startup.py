from os import path
from configuration import Configuration as IConfiguration
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from data.applicationDbContext import context
import logging.config
import logging

class Startup:

    settings: IConfiguration = IConfiguration()
    _logger:  logging.Logger

    def ConfigureServices(self):

        # try connecting to the database
        try:
            context.client = AsyncIOMotorClient(self.settings.GetDefaultConnection())
            context.database = self.settings.GetDefaultDatabase()
            self._logger.info(f"Connected to {self.settings.GetDefaultDatabase()}")
        except Exception as e:
            self._logger.error(f"Error connecting to {self.settings.GetDefaultDatabase()}: {e}")
            raise e

    def Configure(self, app: FastAPI):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
        return app

    def __init__(self, app: FastAPI) -> None:
        #self.settings = AppSettings()
        print(f"Settings: {self.settings.Title}")
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'customLogging/logging.conf')
        logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
        self._logger = logging.getLogger(__name__)
        self.ConfigureServices()
        # self.Configure(app)