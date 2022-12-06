# Description: This is the main script that gets the visitor count and updates it for website
# Designed by: Olin Osborne III
# Date: 12/2/2022
# Version: 2.0
from update_visitor_count import update_count
import json

database_name = 'visitor-count-DB'


# main lambda event handler for API requests
def lambda_handler(event, context):
    # Receives event and determines which route it is coming from
    if event['routeKey'] == 'GET /visitor-count':
        # Gets visitor count from Database
        response = update_count(database_name)
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': 'https://olins-resume.com/',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods' : "GET",
            'Access-Control-Allow-Credentials': '*',
            'Content-Type': 'application/json'},
            'body': response}
    # If no known route returns client Error
    else:
        response = json.dumps(event)
        return {'statusCode': 400, 'body': json.dumps('Request Failed.')}, response