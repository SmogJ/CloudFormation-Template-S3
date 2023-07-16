import requests
import openpyxl
import os

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

# S3 url imported from env
s3_bucket_url = os.getenv("S3_URL")

# Enter S3 bucket URL/filename
if s3_bucket_url is None:
    print('S3 url not found. Make sure you have set the environment variable.')

# Load Excel workbook
workbook = openpyxl.load_workbook('DATA/MOCK_DATA.xlsx')  

# Select the desired sheet by name or index
sheet = workbook['MOCK_DATA'] 

# Data
user_data={}
count=0

# iterate through the columns of the sheet
for col in sheet.iter_cols(values_only=True):
    # user_data[col[0]]=[value for value in col[1:]]
    count+=1
    user_data[col[0]]= col[count]
    

# Close the workbook
workbook.close()
    

def send_user_data_to_s3(user_data, s3_bucket_url):
    api_key= os.getenv("POSTMAN_API_KEY")
    

    if api_key is None:
        print('Postman API key not found. Make sure you have set the environment variable.')

    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key  # Replace with your Postman API key
    }
    
    response = requests.put(s3_bucket_url, json=user_data, headers=headers)
    
    if response.status_code == 200:
        print('User data sent successfully to S3!')
    else:
        print('Failed to send user data to S3. Error:', response.text) 


send_user_data_to_s3(user_data, s3_bucket_url)