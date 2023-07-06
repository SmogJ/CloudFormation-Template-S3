import requests
import openpyxl
import os

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

def send_user_data_to_s3(user_data, s3_bucket_url):
    ApiKey= os.getenv("POSTMAN_API_KEY.env")

    if api_key is None:
        print('Postman API key not found. Make sure you have set the environment variable.')
    return

    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': ApiKey  # Replace with your Postman API key
    }
    
    response = requests.post(s3_bucket_url, json=user_data, headers=headers)
    
    if response.status_code == 200:
        print('User data sent successfully to S3!')
    else:
        print('Failed to send user data to S3. Error:', response.text)


# Load Excel workbook
workbook = openpyxl.load_workbook('Data\MOCK_DATA.xlsx')  

# Select the desired sheet by name or index
sheet = workbook['MOCK-DATA']  

# Data
# user_data = data

# Iterate through each row in the sheet
for col in sheet.iter_cols(values_only=True):
    # Access the cell values in each row
    for cell_value in col:
        user_data={col[0]:cell_value}

# Close the workbook
workbook.close()

# Enter S3 bucket URL/filename
s3_bucket_url = 's3://user-data-container/mock-file-3.txt'  

send_user_data_to_s3(user_data, s3_bucket_url)
