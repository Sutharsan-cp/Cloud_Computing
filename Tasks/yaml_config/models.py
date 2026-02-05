from pydantic import BaseModel, Field
from typing import Dict

class AppInfo(BaseModel):
    name: str
    version: str
    mode: str

class Network(BaseModel):
    host: str
    port: int

class Database(BaseModel):
    host: str
    port: int
    name: str
    user: str

class Logging(BaseModel):
    level: str
    file: str

class Features(BaseModel):
    new_ui: bool = Field(False)
    beta_api: bool = Field(False)

class Config(BaseModel):
    app: AppInfo
    network: Network
    database: Database
    logging: Logging
    features: Features
