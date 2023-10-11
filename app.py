import json
import boto3

def lambda_handler(event, context):
    # Select the region you would like to list function concurrency
    region = "region"

    lambda_client = boto3.client('lambda', region_name=region)
    count = 0