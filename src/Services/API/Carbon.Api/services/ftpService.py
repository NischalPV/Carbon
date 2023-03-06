from logging import Logger
from typing import Any
from uuid import uuid4
import aioftp

from fastapi import Depends, UploadFile
from configuration import Configuration as IConfiguration
from customLogging.logger import ILogger
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from data.applicationDbContext import getDbContext
from data.repository import Repository
from entities.fileEntity import FileEntity

class FtpService:

    
    _ftpSetting: Any
    _ftpHost: str
    _ftpPort: int
    _ftpUsername: str
    _ftpKey: str
    _logger = None

    _dbContext: AsyncIOMotorClient  
    database: str
    collection: str = "UploadedFiles"
    _context = None
    _service: Repository[FileEntity]

    def __init__(self, context: tuple[AsyncIOMotorClient, str] = Depends(getDbContext), logger: Logger = Depends(ILogger)) -> None:
        self._logger = logger
        settings: IConfiguration = IConfiguration()
        self._ftpSetting = settings.FTPCredentials
        self.__setFtpCredentials()
        self._logger.info("FtpService initialized")

        self._dbContext, self.database = context
        self._context: AsyncIOMotorCollection = self._dbContext[self.database][self.collection]
        self._service = Repository[FileEntity](self._context, self._logger)
        self._logger.info("Connected to database")

    def __setFtpHost(self) -> str:
        self._ftpHost = self._ftpSetting['FTPHost']

    def __setFtpPort(self) -> int:
        self._ftpPort = self._ftpSetting['FTPPort']

    def __setFtpUsername(self) -> str:
        self._ftpUsername = self._ftpSetting['FTPUsername']

    def __setFtpKey(self) -> str:
        self._ftpKey = self._ftpSetting['FTPKey']

    def __setFtpCredentials(self) -> None:
        self.__setFtpHost()
        self.__setFtpPort()
        self.__setFtpUsername()
        self.__setFtpKey()

    
    def __createFileEntityInstance(self, file: UploadFile, filename: str) -> FileEntity:
        return FileEntity(
            Name=filename,
            Extension=file.filename.split('.')[-1],
            Size=file.file.tell(),
            Path=f"{self._ftpHost}/uploads/{filename}"
            )

    async def __saveFileToDatabase(self, file: UploadFile, filename: str):
        self._logger.info(f"Saving file {file.filename}...")

        newUploadedFile = self.__createFileEntityInstance(file, filename)
        uploadedFile = await self._service.AddAsync(newUploadedFile)

        return FileEntity(**uploadedFile) if uploadedFile else None

    # Uploads a file to the FTP server
    async def uploadFileTpFtp(self, file: UploadFile):
        """
        Uploads a file to the FTP server
        
        :param file: The file to upload
        :type file: UploadFile
        :return: True if the file was uploaded successfully, False otherwise
        :rtype: bool

        """
        specialCharacters=['@','#','$','*','&', ' ']
        normalizedFilename = "".join(filter(lambda char: char not in specialCharacters , file.filename))
        try:

            async with aioftp.Client.context(self._ftpHost, self._ftpPort, self._ftpUsername, self._ftpKey) as client:
                async with client.upload_stream(f"uploads/{normalizedFilename}") as stream:
                    await stream.write(file.file.read())

            uploadedfile = await self.__saveFileToDatabase(file, normalizedFilename)
            self._logger.info(f"File {file.filename} uploaded successfully")

            return uploadedfile

        except Exception as e:
            self._logger.error(f"Error uploading file to ftp: {e}")
            return False

    # Downloads a file from the FTP server
    async def readFileFromFtp(self, filename: str) -> Any | None:
        """
        Reads a file from the FTP server
        
        :param filename: The name of the file to download
        :type filename: str
        :return: The file contents if the file was downloaded successfully, None otherwise
        :rtype: Any | None
        """
        try:
            async with aioftp.Client.context(self._ftpHost, self._ftpPort, self._ftpUsername, self._ftpKey) as client:
                async with client.download_stream(filename) as stream:
                    return await stream.read()

        except Exception as e:
            self._logger.error(f"Error reading file from ftp: {e}")
            return None



