import numpy as np
import pandas as pd
import json


def process_input(request_data: str):
    """
    asserts that the request data is correct.
    :param request_data: data gotten from the request made to the API
    :return: the numpy array of the request.data input
    """
    parsed_body = json.loads(request_data)
    assert len(parsed_body) >= 1 #request_data must be a dictionary (or dictionaries) with 13 features
    data = pd.DataFrame(parsed_body, columns=["CRIM", 
                                                "ZN", 
                                                "INDUS", 
                                                "CHAS", 
                                                "NOX", 
                                                "RM", 
                                                "AGE", 
                                                "DIS", 
                                                "RAD", 
                                                "TAX", 
                                                "PTRATIO", 
                                                "B", 
                                                "LSTAT", 
                                                "TARGET"])

    return data.values
