from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession


from app.database import get_session
from app import schemas
from app import DAO


router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.get("/", response_model=list[schemas.IncidentOut])
async def get_incidents(session: AsyncSession = Depends(get_session), status: schemas.StatusEnum | None = None,):
    return await DAO.get_incidents(session, status)

@router.post("/", response_model=schemas.IncidentOut, status_code=status.HTTP_201_CREATED)
async def create_incident(payload: schemas.IncidentCreate, session: AsyncSession = Depends(get_session),):
    return await DAO.create_incident(session, payload)

@router.patch("/{incident_id}", response_model=schemas.IncidentOut)
async def update_incident_status(incident_id: int, payload: schemas.IncidentUpdateStatus, session: AsyncSession = Depends(get_session),):
    incident = await DAO.update_incident_status(session, payload, incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident