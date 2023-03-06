from fastapi import Depends, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends, Response, status

from controllers.baseController import BaseController
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from services.ftpService import FtpService

router = InferringRouter(
    tags=["files"],
    responses={404: {"description": "Not found"}},
)

@cbv(router)
class FileController(BaseController):

    _service: FtpService = Depends(FtpService)

    @router.post("/upload")
    async def upload_file(self, file: UploadFile = File(...)):
        """
        Uploads a file to the FTP server
        
        :param file: The file to upload
        :type file: UploadFile
        :return: True if the file was uploaded successfully, False otherwise
        :rtype: bool
        """

        result = await self._service.uploadFileTpFtp(file)

        return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder({"result": result})) if result else JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"Error": "Error uploading file!"})

