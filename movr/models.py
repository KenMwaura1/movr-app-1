"""
Aligns sqlalchemy's schema for the "vehicles" table with the database.
"""

from sqlalchemy import (Boolean, Column, DateTime, Float, Integer,
                        PrimaryKeyConstraint, String, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

Base = declarative_base()


class Vehicle(Base):
    """
    DeclarativeMeta class for the vehicles table.

    Arguments:
        Base {DeclarativeMeta} -- Base class for model to inherit.
    """
    __tablename__ = 'vehicles'
    id = Column(UUID(as_uuid=True), server_default=func.uuid_generate_v4(), )
    last_longitude = Column(Float)
    last_latitude = Column(Float)
    last_checkin = Column(DateTime, default=func.now)
    in_use = Column(Boolean)
    vehicle_type = Column(String)
    battery = Column(Integer)
    PrimaryKeyConstraint(id)

    def __repr__(self):
        return "<Vehicle(id='{0}', vehicle_type='{1}')>".format(
            self.id, self.vehicle_type)

class LocationHistory(Base):
    """
    Table object to store a vehicle's location_history
    Arguments:
        Base {DeclarativeMeta} -- Base class for declarative SQLAlchemy class
                that produces appropriate `sqlalchemy.schema.Table` objects.
    """
    __tablename__ = 'location_history'
    id = Column(UUID(as_uuid=True), server_default=func.uuid_generate_v4(), )
    vehicle_id = Column(UUID(as_uuid=True), ForeignKey('vehicles.id'))
    longitude = Column(Float)
    latitude = Column(Float)
    timestamp = Column(DateTime, default=func.now)
    PrimaryKeyConstraint(id)

    def __repr__(self):
        return (("<Vehicle(id='{0}', vehicle_id='{1}', ts='{2}', "
                 "longitude='{3}', latitude='{4}')>"
                 ).format(self.id, self.vehicle_id, self.ts, self.longitude,
                          self.latitude))