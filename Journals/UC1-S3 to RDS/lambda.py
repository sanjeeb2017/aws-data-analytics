import json
import boto3
import os
import mysql.connector
import sys
import logging
import csv
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Connection String Details - Define as part of environmental variable details.
host = os.environ["host"]
port = os.environ["port"]
database = os.environ["database"]
username = os.environ["username"]
password = os.environ["password"]

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key_name = event['Records'][0]['s3']['object']['key']
    
    s3_client = boto3.client('s3')
    
    s3_file_path = bucket_name + '/' + file_key_name
    
    
    try:
       # connection = create_mysql_DBconnection()
        connection = mysql.connector.connect(user=username,password=password,host=host,port=port,database=database)
        file_object = s3_client.get_object(Bucket=bucket_name,Key=file_key_name)
        record_lines = file_object['Body'].read().decode('utf-8').split()
        records = []
        for line in csv.DictReader(record_lines):
            record_value =list(line.values())
            records.append(record_value)
    
        
        insert_statement="insert into demo_data (roll_no,name) values (%s,%s);"
        cs = connection.cursor()
        print("Executing....")
        cs.executemany(insert_statement,records)
        cs.close()
        connection.commit()
    except Exception as e:
        logger.info("###### Database Exception Occurred ######*")
        logger.error(str(e))
    

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
