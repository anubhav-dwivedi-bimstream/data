import requests


response = requests.get("https://theastrotime.com/index.html")
print(response.status_code)
print(response.text[:200])
# Analyze response details
print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"Encoding: {response.encoding}")
print(f"Content Length: {len(response.content)}")
