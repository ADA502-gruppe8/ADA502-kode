from sqlalchemy import Column, ForeignKey, Integer, Numeric, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    latitude = Column(Numeric(9,6))
    longitude = Column(Numeric(9,6))
    weather_observations = relationship("WeatherObservation", back_populates="location")
    weather_forecasts = relationship("WeatherForecast", back_populates="location")
    fire_risk_predictions = relationship("FireRiskPrediction", back_populates="location")

class WeatherObservation(Base):
    __tablename__ = 'weather_observations'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    temperature = Column(Numeric(4,2))
    humidity = Column(Numeric(5,2))
    wind_speed = Column(Numeric(4,2))
    location = relationship("Location", back_populates="weather_observations")

class WeatherForecast(Base):
    __tablename__ = 'weather_forecasts'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    temperature = Column(Numeric(4,2))
    humidity = Column(Numeric(5,2))
    wind_speed = Column(Numeric(4,2))
    location = relationship("Location", back_populates="weather_forecasts")

class FireRiskPrediction(Base):
    __tablename__ = 'fire_risk_predictions'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    fire_risk_score = Column(Numeric)
    location = relationship("Location", back_populates="fire_risk_predictions")


    #Pydantic models
    # API/db/firerisk/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class LocationBase(BaseModel):
    latitude: float
    longitude: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True

class WeatherObservationBase(BaseModel):
    location_id: int
    timestamp: datetime
    temperature: float
    humidity: float
    wind_speed: float

class WeatherObservationCreate(WeatherObservationBase):
    pass

class WeatherObservation(WeatherObservationBase):
    id: int

    class Config:
        orm_mode = True

class WeatherForecastBase(BaseModel):
    location_id: int
    timestamp: datetime
    temperature: float
    humidity: float
    wind_speed: float

class WeatherForecastCreate(WeatherForecastBase):
    pass

class WeatherForecast(WeatherForecastBase):
    id: int

    class Config:
        orm_mode = True

class FireRiskPredictionBase(BaseModel):
    location_id: int
    timestamp: datetime
    fire_risk_score: float

class FireRiskPredictionCreate(FireRiskPredictionBase):
    pass

class FireRiskPrediction(FireRiskPredictionBase):
    id: int

    class Config:
        orm_mode = True