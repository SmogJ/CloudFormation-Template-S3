import json
import boto3

# s3= boto3.resource('s3')
s3_client= boto3.client('s3')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-store')

# bucket= s3.Bucket('user-data-container')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]["s3"]["bucket"]["name"]
    s3_file_name = event['Records'][0]["s3"]["object"]["key"]
    response = s3_client.get_object(Bucket='user-data-store', Key='mock-file-3.txt')
    
    # decode the data and split the data in the json to a newline
    # user = response['Body'].read().decode('utf-8')
    user= json.loads(response['Body'].read())


    # Raise Exception when inputing data
    try:
        response= table.put_item(Item=user)
        print('Data inserted successfully into DynamoDB:', response)
    except Exception as e:
        print('Failed to insert data into DynamoDB:', e)
    
    
    return{
        'statusCode': 200,
        'body': json.dumps('Items added successfully!'),
        # 'data': user
    }