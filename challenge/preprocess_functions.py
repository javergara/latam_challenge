""" This module contains the functions to preprocess the data. """

from datetime import datetime


def get_min_diff(data: dict) -> float:
    """Get the difference in minutes between two dates.

    Args:
        data (dict): Dictionary with two dates.

    Returns:
        float: Difference in minutes.
    """
    fecha_o = datetime.strptime(data["Fecha-O"], "%Y-%m-%d %H:%M:%S")
    fecha_i = datetime.strptime(data["Fecha-I"], "%Y-%m-%d %H:%M:%S")
    min_diff = ((fecha_o - fecha_i).total_seconds()) / 60

    return min_diff
