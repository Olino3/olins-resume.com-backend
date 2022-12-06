# Description: get_visitor_count a set of functions that get items from database
# Designed by: Olin Osborne III
# Date: 12/2/2022
# Version: 2.5
import boto3
import botocore
from botocore.exceptions import ClientError
import json


# scan_db scans the entire database and returns all items can be used with filters
def scan_db(table, scan_kwargs=None):
    """
    Get all records of the dynamodb table where the FilterExpression holds true
    :param scan_kwargs: Used to pass filter conditions, know more about kwargs- geeksforgeeks.org/args-kwargs-python/
    :type scan_kwargs: dict
    :param table: dynamodb table name
    :type table: str
    :return: list of records
    :rtype: dict
    """
    if scan_kwargs is None:
        scan_kwargs = {}
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    complete = False
    records = []
    while not complete:
        try:
            response = table.scan(**scan_kwargs)
        except botocore.exceptions.ClientError as error:
            raise Exception('Error quering DB: {}'.format(error))

        records.extend(response.get('Items', []))
        next_key = response.get('LastEvaluatedKey')
        scan_kwargs['ExclusiveStartKey'] = next_key

        complete = True if next_key is None else False
    return records


# get_specific_item gets a specific item by key ID
def get_specific_item(database_name):
    dynamodb = boto3.resource(
        'dynamodb')
    # Specify the table to read from
    visitor_count_table = dynamodb.Table(database_name)
    # Gets specific item by key ID requires key ID will return error
    try:
        response = visitor_count_table.get_item(
            Key={'site_id': 'main page'})
    except ClientError as e:
        return {json.dumps("Item not found. Key ID is invalid.")}
    else:
        item = response['Item']
        return item['visitors']
