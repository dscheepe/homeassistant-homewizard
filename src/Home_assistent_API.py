import requests
import keyring

token = keyring.get_password("HomeAssistant", "api_token")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

r = requests.get(
    "http://homeassistant.local:8123/api/states",
    headers=headers
)

print(r.json())