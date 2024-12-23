""" This module contains the schemas for the API """

from typing import List

from pydantic import BaseModel


class FlightData(BaseModel):
    """Schema for the flight data"""

    OPERA: str
    TIPOVUELO: str
    MES: int


class PredictionRequest(BaseModel):
    """Schema for the prediction request"""

    flights: List[FlightData]
