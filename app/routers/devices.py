from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_analysis import data_analysis
from app.db_conn import get_async_session
from app.models import DeviceData
from app.schemas import DeviceDataSch

router = APIRouter(
    prefix='/devices',
    tags=["Data from device"]
)

@router.post("/add_data")
async def add_device_data(new_data: DeviceDataSch, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(DeviceData).values(**new_data.dict())
    await session.execute(stmt)
    await session.commit()

    return {'status': 'successes'}

@router.get("/all_time")
async def get_all_time_data(device_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(DeviceData).where(DeviceData.device_id == device_id).order_by(DeviceData.id)
    res = await session.execute(query)
    data = res.scalars().all()

    return data_analysis(data)

@router.get("/period")
async def get_period_data(device_id: int, start_period: datetime, stop_period: datetime,
                          session: AsyncSession = Depends(get_async_session)):
    query = select(DeviceData).\
        where((DeviceData.date >= start_period) & (DeviceData.date <= stop_period) & (DeviceData.device_id == device_id)).\
        order_by(DeviceData.id)
    res = await session.execute(query)
    data = res.scalars().all()

    return data_analysis(data)
