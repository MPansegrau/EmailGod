import boto3, os
from ..config import settings

s3 = boto3.client('s3', region_name=settings.aws_region)

def put_object(key: str, data: bytes, content_type: str):
    s3.put_object(Bucket=settings.aws_bucket, Key=key, Body=data, ContentType=content_type)
    return f"s3://{settings.aws_bucket}/{key}"
