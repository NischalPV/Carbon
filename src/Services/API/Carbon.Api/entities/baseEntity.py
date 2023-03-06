from datetime import datetime
import uuid
from pydantic import BaseModel, Field

class BaseEntity(BaseModel):
    Id: str = Field(default_factory=uuid.uuid4, alias="_id")
    CreatedDate: datetime = datetime.utcnow()
    ModifiedDate: datetime = None
    IsActive: bool = True