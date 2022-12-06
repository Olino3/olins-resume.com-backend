# Description: update_visitor_count is a set of functions that updates the count in the database
# Designed by: Olin Osborne III
# Date: 12/2/2022
# Version: 2.2
import json
import boto3
from get_visitor_count import get_specific_item


# put item puts an item or set of items into database based on a primary key
def update_count(database_name):
    dynamodb = boto3.resource('dynamodb')
    # Specify the table
    table = dynamodb.Table(database_name)
    new_visitor_count = get_specific_item(database_name) + 1
    # tests whether items can be placed in database
    response = table.put_item(Item= {'site_id' : 'main page', 'visitors': new_visitor_count})
    return get_specific_item(database_name)
