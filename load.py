import pandas as pd
import numpy as np


def load(path: str):
    """
    Takes a path as argument, writes the dimensions of the data set
    and returns it
    """
    try:
        assert type(path) is str, "invalid arg"
        file = pd.read_csv(path)
        np_array = file.to_numpy()
        return file
    except Exception as msg:
        print("Error:", msg)
    return None
