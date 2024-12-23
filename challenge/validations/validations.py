""" Validations for the challenge app. """

import pandas as pd
from fastapi import HTTPException

from challenge.constants import TOP_10_FEATURES


def validate_request(data: pd.DataFrame) -> None:
    """Validate the request data.

    Args:
        data (pd.DataFrame): request data.

    Raises:
        ValueError: if the data is invalid.
    """
    if not data.columns.isin(TOP_10_FEATURES).all():
        raise HTTPException(status_code=400, detail="Unknown columns in the request.")


def validate_month_data(data: pd.DataFrame) -> None:
    """Validate the month data.

    Args:
        data (pd.DataFrame): request data.

    Raises:
        ValueError: if the data is invalid.
    """
    if not data["MES"].isin(range(1, 13)).all():
        raise HTTPException(status_code=400, detail="Invalid month in the request.")
