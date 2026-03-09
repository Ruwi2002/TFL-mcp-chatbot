import requests

url = "https://api.tfl.gov.uk/Line/central/Status"

response = requests.get(url)

print(response.json())
