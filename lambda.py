import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            source_bucket = record['s3']['bucket']['name']
            source_key = record['s3']['object']['key']
            
            destination_bucket = 's3-finish'
            copy_source = {'Bucket': source_bucket, 'Key': source_key}
            
            response = s3.copy_object(Bucket=destination_bucket, Key=source_key, CopySource=copy_source)
            logger.info(f"Object copied: {source_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('File copied successfully!')
        }
    except Exception as e:
        logger.error(f"Error copying object: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
