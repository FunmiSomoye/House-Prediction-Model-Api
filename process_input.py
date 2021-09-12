import numpy as np
import json


def process_input(request_data: str) -> np.array:
    """
    asserts that the request data is correct.
    :param request_data: data gotten from the request made to the API
    :return: the numpy array of the request.data input
    """
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body) >= 1 #"'inputs' must be a 1-D array with 13 parameters"
    return parsed_body