import json
from typing import Any

class Configuration:
    DefaultConnection: str
    DefaultDatabase: str
    Settings: Any
    ConnectionStrings: Any
    Title: str
    Host: str
    Port: int
    Debug: bool
    
    FTPCredentials: Any
    FTPHost: str
    FTPPort: int
    FTPUsername: str
    FTPKey: str

    IdentityUrl: str
    ExternalIdentityUrl: str
    EventBusConnection: str
    OAuthClientId: str

    def __init__(self):

        
        try:
            with open('appSettings.json', 'r') as f:

                # Load Default Connection String from appSettings.json

                #print("Loading appSettings.json")
                self.Settings = json.load(f)
                self.ConnectionStrings = self.Settings['ConnectionStrings']
                self.DefaultConnection = self.ConnectionStrings['DefaultConnection']
                self.DefaultDatabase = self.ConnectionStrings['DefaultDatabase']
                self.Title = self.Settings['AppTitle']
                self.Host = self.Settings['Host']
                self.Port = self.Settings['Port']
                self.Debug = self.Settings['Debug']

                # Load FTP Connection settings from appSettings.json
                self.FTPCredentials = self.Settings['FTPCredentials']
                self.FTPHost = self.FTPCredentials['FTPHost']
                self.FTPPort = self.FTPCredentials['FTPPort']
                self.FTPUsername = self.FTPCredentials['FTPUsername']
                self.FTPKey = self.FTPCredentials['FTPKey']

                # Load Identity Server settings from appSettings.json
                self.IdentityUrl = self.Settings['IdentityUrl']
                self.ExternalIdentityUrl = self.Settings['ExternalIdentityUrl']
                self.EventBusConnection = self.Settings['EventBusConnection']
                self.OAuthClientId = self.Settings['OAuthClientId']



        except Exception as e:
            self.Settings = {}
            self.ConnectionStrings = {}
            self.DefaultConnection = ''
            self.DefaultDatabase = ''
            self.Title = ''
            self.Host = ''
            self.Port = 8000
            self.Debug = True
            self.FTPCredentials = {}
            self.FTPHost = ''
            self.FTPPort = 21
            self.FTPUsername = ''
            self.FTPKey = ''
            self.IdentityUrl = ''
            self.ExternalIdentityUrl = ''
            self.EventBusConnection = ''
            self.OAuthClientId = ''
            
            print(e)
            

    def GetDefaultConnection(self):
        return self.DefaultConnection

    def GetDefaultDatabase(self):
        return self.DefaultDatabase

    def GetDefaultFtpCredentials(self):
        return self.FTPCredentials
