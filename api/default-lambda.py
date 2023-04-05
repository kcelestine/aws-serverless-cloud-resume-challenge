import boto3

dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("cloud-resume-stats")

def lambda_handler(event, context):
    
    response = table.get_item(
        Key={
        'stat': 'view-count'
        }
    )
    visitor_count = response['Item']['num']
    visitor_count += 1
    
    response = table.put_item(
        Item = {
            'stat': 'view-count',
            'num': visitor_count
        }
    )
    
    return {
        "statusCode": 200,
        "headers": {
			"Content-Type": "application/json",
			"Access-Control-Allow-Headers": "Content-Type",
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Methods": "OPTIONS,GET",
		},
        "body": visitor_count
    }
