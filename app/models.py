from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeviceData(Base):
    __tablename__ = 'device_data'

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)
    date = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
