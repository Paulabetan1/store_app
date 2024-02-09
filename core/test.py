import requests

url = 'http://microservices.dev.rappi.com/api/paps/auth/token'

payload = {
 "client_id": "u37ZvpV04mkX6UiUVgMY4rd4CGxAU27m",
 "client_secret": "8iXy7uIoGELOZ29CZh6LkEXCY-WIXpTK_sRZgqb78-RVeGqVGm9H5kHxf3AZDNZc"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.content)