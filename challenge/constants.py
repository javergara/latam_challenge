""" Constants file."""

TOP_10_FEATURES = [
    "OPERA_Latin American Wings",
    "MES_7",
    "MES_10",
    "OPERA_Grupo LATAM",
    "MES_12",
    "TIPOVUELO_I",
    "MES_4",
    "MES_11",
    "OPERA_Sky Airline",
    "OPERA_Copa Air",
]

THRESHOLD_IN_MINUTES = 15

LATEST_MODEL_PATH = "models/model_latest.joblib"

HTML_HOME_CONTENT = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flight Delay Prediction API</title>
    </head>
    <body>
        <h1>Welcome to the Flight Delay Prediction API</h1>
        <p><strong>Documentation:</strong> <a href="/docs">Find documentation at /docs</a></p>
    </body>
    </html>
    """
