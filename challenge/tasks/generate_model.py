""" Task to generate a model from the data. """

import pandas as pd

from challenge.model import DelayModel

if __name__ == "__main__":
    data = pd.read_csv(filepath_or_buffer="data/data.csv")
    model = DelayModel()
    features, target = model.preprocess(data=data, target_column="delay")
    model.fit(features=features, target=target)
    model.export_model()
