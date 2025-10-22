from pydantic import BaseModel
from typing import Optional
from uuid import UUID


# response models
class DashboardOut(BaseModel):
    id: UUID
    name: str
    description: str = ''
    app_id: Optional[UUID] = None
    updated_at: str = 'Wed, 01 Jan 2021 16:12:07 GMT'
    created_at: str = 'Wed, 01 Jan 2021 16:12:07 GMT'


# request models
class DashboardUpdateIn(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class DashboardCreateIn(BaseModel):
    name: str
    description: Optional[str] = None
    app_id: Optional[UUID]
