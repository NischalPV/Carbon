from pydantic import Extra
from entities.baseEntity import BaseEntity


class FileEntity(BaseEntity):
    Name: str
    Extension: str
    Size: int
    Path: str

    class Config:
        allow_population_by_field_name = True
        extra = Extra.forbid
        arbitary_types_allowed = True