from fastapi import Depends, FastAPI

from configuration import Configuration as IConfiguration
from data.applicationDbContext import context
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2AuthorizationCodeBearer
from controllers.fileController import router as fileRouter

from startup import Startup

appSettings = IConfiguration()

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="http://localhost:5022/connect/authorize",
    tokenUrl="http://localhost:5022/connect/token",
    scopes={"API": "API Scope"},

)

app = FastAPI(dependencies=[Depends(oauth2_scheme)])
              
app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )


# appStartup = Startup(app)

app.include_router(fileRouter, prefix="/api/v1/files")

@app.on_event("startup")
async def startup():
    Startup(app)
    

@app.on_event("shutdown")
async def shutdown():
    context.client.close()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host=appSettings.Host, port=appSettings.Port, reload=appSettings.Debug)