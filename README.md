# House-Prediction-Model-Api

## Description
This project is about creating an endpoint that predicts house prices based on inputed features

## Getting Started
### Endpoint
Using this API is very simple.

The API can be found on [Funmi's House Prediction Api](https://funmi-house-prices-predict-api.herokuapp.com/) and has just one useful endpoint: [predict](https://funmi-house-prices-predict-api.herokuapp.com/predict)

The endpoint `/predict` accepts payload of the following structure.
``` http
POST /api/predict/
```
|Parameter |  Type                  |  Description           |
|----------|:----------------------:|-----------------------:|
| `inputs` |  `list of dictionaries` | Features according to columns [here](https://scikit-learn.org/stable/datasets/toy_dataset.html#boston-dataset)|


## Responses
sucesss response
`{'predicted_class': [21.197123104871295, 21.197123104871295]}`


## Example Payload
Calling the endpoint `/api/predict/` with a 2x2 array. 
``` javascript
import requests
import json

list_of_dict = {"inputs":[{"CRIM": 7.83932, 
                     "ZN": 0.0,
                     "INDUS": 18.10,
                     "CHAS": 0.0,
                     "NOX": 0.655,
                     "RM": 6.209,
                     "AGE": 65.4,
                     "DIS": 2.9634,
                     "RAD": 24.0,
                     "TAX": 666.0,
                     "PTRATIO": 20.2,
                     "B": 396.90,
                     "LSTAT": 13.22},
                     {"CRIM": 7.83932, 
                     "ZN": 0.0,
                     "INDUS": 18.10,
                     "CHAS": 0.0,
                     "NOX": 0.655,
                     "RM": 6.209,
                     "AGE": 65.4,
                     "DIS": 2.9634,
                     "RAD": 24.0,
                     "TAX": 666.0,
                     "PTRATIO": 20.2,
                     "B": 396.90,
                     "LSTAT": 13.22
                     }]}
                     
resp = requests.post("https://funmi-house-prices-predict-api.herokuapp.com/predict", 
                     data=json.dumps(list_of_dict))
print(json.loads(resp.text))
                  
```
