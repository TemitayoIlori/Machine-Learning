import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://ed717147-f038-4a5f-bece-b3ecd4099a2d.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "cpVQN8VGdUZViX3Ifp71O89CbKeSd6sm"

# Two sets of data to score, so we get two results back
data = {
    "data": [
        {
            "age": 54,
            "job": "services",
            "marital": "married",
            "education": "basic.9y",
            "default": "no",
            "housing": "yes",
            "loan": "yes",
            "contact": "cellular",
            "month": "jul",
            "day_of_week": "fri",
            "duration": 500,
            "campaign": 1,
            "pdays": 999,
            "previous": 0,
            "poutcome": "failure",
            "emp.var.rate": -1.8,
            "cons.price.idx": 93.465,
            "cons.conf.idx": -41.8,
            "euribor3m": 4.96,
            "nr.employed": 5191,
        },
    ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
