import json
import base64
from urllib.parse import unquote


def lambda_handler(event, context):
    print(event)

    body = event['body']
    isBase64Encoded = event['isBase64Encoded']

    # check if event body was decoded
    if isBase64Encoded:
        decoded_data = base64.b64decode(body)
        decoded_data = unquote(decoded_data)

        # parse body when event was generated by command '/start'
        if decoded_data.startswith('token'):
            items_list = list()
            for item in decoded_data.split('&'):
                item = tuple(item.split('='))
                items_list.append(item)
            body = dict(items_list)

        # parse body when event was generated clicking on the button
        elif decoded_data.startswith('payload'):
            body = json.loads(decoded_data.split('=')[1])

    print(body)

    # when the simple message was written to the chat do smth
    if 'event' in body:
        print('1')

    # when the command was called in the chat
    elif 'command' in body:
        print('2')
        return {
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

    # when the button was clicked in the chat
    elif 'actions' in body:
        print('3')

    return {
        'status_code': 200
    }
