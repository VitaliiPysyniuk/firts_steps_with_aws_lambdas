import datetime
import json


def handler(event, context):
    http_context = event['requestContext']['http']
    response_data = dict()

    print("Executed at: ", datetime.datetime.now())
    print('\n-----------------------------------------------------\n')
    if http_context["method"] == 'GET':

        print('Processed HTTP GET method')
        response_data['method'] = http_context["method"]
    elif http_context["method"] == 'POST':
        body = json.loads(event['body'])
        print('Processed HTTP POST method')
        response_data['method'] = http_context["method"]
        response_data['body'] = body
    elif http_context["method"] == 'PATCH':
        body = json.loads(event['body'])
        path_params = event['pathParameters']
        print('Processed HTTP PATCH method')
        response_data['method'] = http_context["method"]
        response_data['path_params'] = path_params
        response_data['body'] = body
    elif http_context["method"] == 'DELETE':
        path_params = event['pathParameters']
        print('Processed HTTP DELETE method')
        response_data['method'] = http_context["method"]
        response_data['path_params'] = path_params
    print('\n-----------------------------------------------------')

    response = {
        'statusCode': 200,
        'body': json.dumps(response_data)
    }

    return response

