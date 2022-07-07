from slack_sdk import WebClient

client = WebClient('xoxb-')
channel_id = ""

result = client.chat_postMessage(
    channel=channel_id,
    text="New Paid Time Off request from",
    blocks=[
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Hi, I'm here. What do you want to do?",
                "emoji": True
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Workers",
                        "emoji": True
                    },
                    "action_id": "workers_button_click"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Requests",
                        "emoji": True
                    },
                    "action_id": "requests_button_click"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Bonuses",
                        "emoji": True
                    },
                    "action_id": "bonuses_button_click"
                }
            ]
        }
    ]
)
print(result)

xx = {
    'blocks': [
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Hi, I'm here. What do you want to do?",
                "emoji": True
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Workers",
                        "emoji": True
                    },
                    "action_id": "workers_button_click"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Requests",
                        "emoji": True
                    },
                    "action_id": "requests_button_click"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Bonuses",
                        "emoji": True
                    },
                    "action_id": "bonuses_button_click"
                }
            ]
        }
    ]
}
