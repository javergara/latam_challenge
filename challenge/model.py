""" Model for predicting flight delays. """


import logging
import os
from datetime import datetime
from typing import List, Tuple, Union

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from challenge.constants import LATEST_MODEL_PATH, THRESHOLD_IN_MINUTES, TOP_10_FEATURES
from challenge.exceptions import LoadModelError
from challenge.preprocess_functions import get_min_diff

logger = logging.getLogger(__name__)


class DelayModel:
    """Model for predicting flight delays."""

    def __init__(self):
        self._model = None  # Model should be saved in this attribute.

    def preprocess(
        self, data: pd.DataFrame, target_column: str = None
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or predict.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """

        features = pd.concat(
            [
                pd.get_dummies(data["OPERA"], prefix="OPERA"),
                pd.get_dummies(data["TIPOVUELO"], prefix="TIPOVUELO"),
                pd.get_dummies(data["MES"], prefix="MES"),
            ],
            axis=1,
        )

        for feature in TOP_10_FEATURES:
            if feature not in features:
                features[feature] = 0

        if target_column is not None:
            data["min_diff"] = data.apply(get_min_diff, axis=1)
            data[target_column] = np.where(
                data["min_diff"] > THRESHOLD_IN_MINUTES, 1, 0
            )

            target = data[[target_column]]

            return features[TOP_10_FEATURES], target

        return features[TOP_10_FEATURES]

    def fit(self, features: pd.DataFrame, target: pd.DataFrame) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.DataFrame): target.
        """
        n_y0 = (target == 0).sum()
        n_y1 = (target == 1).sum()

        self._model = LogisticRegression(
            class_weight={1: n_y0 / len(target), 0: n_y1 / len(target)}
        )
        self._model.fit(features, target)

    def predict(self, features: pd.DataFrame) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.

        Returns:
            (List[int]): predicted targets.

        Raises:
            ValueError: if model has not been trained.
        """
        if self._model is None:
            raise ValueError("Model has not been trained or loaded.")

        return (self._model.predict(features)).tolist()

    def export_model(self) -> None:  # pragma: no cover
        """Save the model to a file."""
        os.makedirs("models", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        versioned_model_path = f"models/model_{timestamp}.joblib"

        joblib.dump(self._model, versioned_model_path)
        joblib.dump(self._model, LATEST_MODEL_PATH)

        logger.info(
            f"Model saved as {versioned_model_path} and updated 'model_latest.joblib'."
        )

    def load_model(self, model_path: str = LATEST_MODEL_PATH) -> None:
        """Load a model from a file.

        Args:
            model_path (str): path to the model file.
        """
        try:
            self._model = joblib.load(model_path)
            logger.info(f"Model loaded from {model_path}.")
        except Exception as error:
            raise LoadModelError(f"Error loading model from {model_path}.") from error
