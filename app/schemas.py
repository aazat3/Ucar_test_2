from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
import enum


class StatusEnum(str, enum.Enum):
    """Incident status"""

    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"

class SourceEnum(str, enum.Enum):
    """Incident source"""

    OPERATOR = "operator" # Пользователь 
    MONITORING = "monitoring" # Автоматичская система мониторинга 
    PARTNER = "partner" # Партнер 

# ---- Incident ----
class IncidentBase(BaseModel):
    text: str = Field(min_length=1, max_length=10_000)
    source: SourceEnum

class IncidentCreate(IncidentBase):
    pass

class IncidentUpdateStatus(BaseModel):
    status: StatusEnum

class IncidentOut(IncidentBase):
    id: int
    status: StatusEnum
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

