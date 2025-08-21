import requests, os

slack_token = ""
channel_id = ""

response = requests.post(
    "https://slack.com/api/chat.postMessage",
    headers={"Authorization": f"Bearer {slack_token}"},
    data={"channel": channel_id, "text": "Hey! I'm Sentinel 🤗, The reason i'm called Sentinel is because I am here to Guard 👮🏻 u from errors. wanna see right? \n"
    "I'm here to let you know if there occurs any failures in your project and share the perfect issues for new people in the team to work upon. Don't worry I won't ping u until required.\nThank me later! 😉"},
)

print(response.json())
