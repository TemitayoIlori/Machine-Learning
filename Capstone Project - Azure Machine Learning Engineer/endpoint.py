import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://a36065b1-5208-4c9f-8e8a-c33de04527a4.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "I74LDyCGmXBt02KLwwAeDWG3V5G1xMNL"

# Two sets of data to score, so we get two results back
data = {
    "data": [
        {
            "MDVP:Fo(Hz)":118.99200,
            "MDVP:Fhi(Hz)":147.30200,
            "MDVP:Flo(Hz)":76.99700,
            "MDVP:Jitter(%)":0.00884,
            "MDVP:Jitter(Abs)":0.00006,
            "MDVP:RAP":0.00470,
            "MDVP:PPQ":0.00564,
            "Jitter:DDP":0.01209,
            "MDVP:Shimmer":0.04274,
            "MDVP:Shimmer(dB)":0.42600,
            "Shimmer:APQ3":0.02282,
            "Shimmer:APQ5":0.03230,
            "MDVP:APQ":0.03071,
            "Shimmer:DDA":0.06645,
            "NHR":0.02411,
            "HNR":22.13300,
            "RPDE":0.424783,
            "DFA":0.805285,
            "spread1":-4.913031,
            "spread2":0.276482,
            "D2":2.401442,
            "PPE":0.294654,
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
