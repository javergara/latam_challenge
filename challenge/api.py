""" FastAPI application for the challenge. """


import logging

import pandas as pd
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from challenge.constants import HTML_HOME_CONTENT, LATEST_MODEL_PATH
from challenge.domain.models import PredictionRequest
from challenge.model import DelayModel
from challenge.validations.validations import validate_month_data, validate_request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(docs_url="/docs")

model = DelayModel()
model.load_model(model_path=LATEST_MODEL_PATH)


@app.get("/", response_class=HTMLResponse)
def get_index() -> str:
    """Index endpoint."""

    return HTML_HOME_CONTENT


@app.get("/health", status_code=status.HTTP_200_OK)
async def get_health() -> dict:
    """Health check endpoint."""
    return {"status": "OK"}


@app.post("/predict", status_code=status.HTTP_200_OK)
async def post_predict(request: PredictionRequest) -> dict:
    """Predict endpoint. Delay prediction for a list of flights.

    Args:
        request (PredictionRequest): request with list of flights.

    Returns:
        dict: prediction for each flight.
    """

    flight_data = request.flights
    data_dicts = [flight.dict() for flight in flight_data]

    data = pd.DataFrame(data_dicts)

    validate_month_data(data=data)

    features = model.preprocess(data=data)

    validate_request(data=features)

    predicted_targets = model.predict(features=features)

    return {"predict": predicted_targets}
