import json
import boto3

# s3= boto3.resource('s3')
s3_client= boto3.client('s3')

dynamodb = boto3.resource('user-data')
table = dynamodb.Table('user-info')

# bucket= s3.Bucket('user-data-container')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]["s3"]["bucket"]["name"]
    s3_file_name = event['Records'][0]["s3"]["object"]["key"]
    response = s3_client.get_object(Bucket='user-data-container', Key='mock-file-3.txt')
    
    # decode the data and split the data in the json to a newline
    user = response['Body'].read().decode('utf-8')
    user= user.split('\n')
    
    # info=[]
    
    for data in user:
        # info.append(data.split(','))
        data= data.split(',')
        try:
            table.put_item(
                item={
                    "id": int(data[0]),
                    "firstname": str(data[1]),
                    "lastname": str(data[2]),
                    "email":data[3],
                    "gender":str(data[4]),
                    "ip_address":data[5],
                    "picture":data[6],
                    "country":data[7],
                    "state": data[8],
                    "address":str(data[9]),
                    })
        except Exception as e:
            raise e 
        # except Exception as err:
        # print (">>>>>>>>"+str(err))
    
    return{
        'statusCode': 200,
        'body': json.dumps('Items added successfully!')
    }