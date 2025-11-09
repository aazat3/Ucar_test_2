from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update


from app import models, schemas


# ---- Incident ----
async def create_incident(session: AsyncSession, payload: schemas.IncidentCreate, ) -> models.Incident:
    incident = models.Incident(text = payload.text, source = payload.source)
    session.add(incident)
    await session.commit()
    await session.refresh(incident)
    return incident

async def get_incidents(session: AsyncSession, status: models.StatusEnum | None = None) -> list[models.Incident]:
    q = select(models.Incident)
    if status:
        q = q.filter(models.Incident.status == status)
    q = q.order_by(models.Incident.created_at.desc())
    res = await session.execute(q)
    return res.scalars().all()

async def update_incident_status(session: AsyncSession, payload: schemas.IncidentUpdateStatus, incident_id: int) -> models.Incident:
    # incident = session.query(models.Incident).filter(models.Incident.id == incident_id).first()
    result = await session.execute(select(models.Incident).filter(models.Incident.id == incident_id).limit(1))
    incident = result.scalar_one_or_none()
    if not incident:
        return None
    incident.status = payload.status
    await session.commit()
    await session.refresh(incident)
    return incident
