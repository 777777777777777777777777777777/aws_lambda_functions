import boto3, os, time

AWS_DEFAULT_REGION = "eu-west-3"
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

bucketname = "lambda.test.on-" + str(time.time())

def lambda_handler(event, context):
     S3 = boto3.resource('s3')  
     try:
         results = S3.create_bucket(
                               Bucket= bucketname,
                               CreateBucketConfiguration={'LocationConstraint':AWS_DEFAULT_REGION}
                               )
         return ("<h1><font color=green>S3 Bucket Create!: </font></h1><br><br>" + str(results))
     except:
         return ("<h1><font color=red>Error!</font></h1><br><br>")