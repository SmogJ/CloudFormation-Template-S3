# Simpe AWS Architecture to Upload data to S3

This is my first cloud project using Amazon Web Service AWS. The project is a simple cloudformation template that provisions an S3 with public access.

In this project I wrote a Python script that upload data using a Postman API to the S3 bucket. The excel data is mock data generated from [mockaroo](https://www.mockaroo.com/). The data contains the following fields:

1. id
2. first_name
3. last_name
4. email
5. gender
6. ip_address
7. picture
8. country
9. state
10. address