import keyring

SERVICE_NAME = "HomeAssistant"
USERNAME = "api_token"

token = input("Voer je Home Assistant token in: ")

keyring.set_password(
    SERVICE_NAME,
    USERNAME,
    token
)

print("Token opgeslagen in Windows Credential Manager.")