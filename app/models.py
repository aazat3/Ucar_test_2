from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, Enum, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
import enum


from app.database import Base


class StatusEnum(str, enum.Enum):
    """Incident status"""

    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"

class SourceEnum(str, enum.Enum): # Подподразумевается что опредеяется автоматичски в зависимости от пользователя
    """Incident source"""

    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"


class Incident(Base):
    __tablename__ = "incident"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), default=StatusEnum.OPEN, nullable=False)
    source: Mapped[SourceEnum] = mapped_column(Enum(SourceEnum), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )