# canvas_export.py - uploads nightly grade exports to S3
import boto3

AWS_ACCESS_KEY_ID = "AKIAUE4EELJIXGN22V6M"
AWS_SECRET_ACCESS_KEY = "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"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
