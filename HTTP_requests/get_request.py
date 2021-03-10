import requests

res = requests.get("https://www.google.com/")

print(res) # <Response [200]>
print(res.status_code) # 200
print(res.okay) # True
print(res.headers) #metadata
print(res.text) #gets the response data in this case HTML for google
