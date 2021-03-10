import requests

url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers={"Accept" : "text/plain"})

response = requests.get(url, headers = { "Accept" : "application/json"})

print(response.text) # this isn't a valid python dictionary, python will consider this as a string
print(response.json()["joke"]) # rhis is a valid python dictionary

