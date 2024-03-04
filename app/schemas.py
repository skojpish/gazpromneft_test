from datetime import datetime

from pydantic import BaseModel


class DeviceDataSch(BaseModel):
    id: int
    device_id: int
    x: float
    y: float
    z: float
    date: datetime
