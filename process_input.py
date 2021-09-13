import numpy as np
import pandas as pd
import json


def process_input(request_data: str) -> pd.DataFrame:
    """
    asserts that the request data is correct.
    :param request_data: data gotten from the request made to the API
    :return: the values from the dataframe 
    """
    
    parsed_body = json.loads(request_data)["inputs"]
    assert len(parsed_body) >= 1 #"'inputs' must be a dictionary (or dictionaries) with 13 features"
    data = {"CRIM": [], 
                     "ZN": [],
                     "INDUS": [],
                     "CHAS": [],
                     "NOX": [],
                     "RM": [],
                     "AGE": [],
                     "DIS": [],
                     "RAD": [],
                     "TAX": [],
                     "PTRATIO": [],
                     "B": [],
                     "LSTAT": []
                     }

    for item in range(len(parsed_body)):
        data["CRIM"].append(parsed_body[item]["CRIM"])
        data["ZN"].append(parsed_body[item]["ZN"])
        data["INDUS"].append(parsed_body[item]["INDUS"])
        data["CHAS"].append(parsed_body[item]["CHAS"])
        data["NOX"].append(parsed_body[item]["NOX"])
        data["RM"].append(parsed_body[item]["RM"])
        data["AGE"].append(parsed_body[item]["AGE"])
        data["DIS"].append(parsed_body[item]["DIS"])
        data["RAD"].append(parsed_body[item]["RAD"])
        data["TAX"].append(parsed_body[item]["TAX"])
        data["PTRATIO"].append(parsed_body[item]["PTRATIO"])
        data["B"].append(parsed_body[item]["B"])
        data["LSTAT"].append(parsed_body[item]["LSTAT"])

    return pd.DataFrame(data)
   
