# Creating a data stream with Kinesis


Here we will create a Data Stream, let's deploy:
* Kinesis Stream
* Kinesis Delivery Stream
* Kinesis Firehose
* LogGroup
* LogStream
* Bucket
* IAM Role
* IAM Policy

Deploy:
1. Navigate to the Cloudformation page on your AWS console
2. Click on create stack -> with new resources
3. Upload the YAML file and follow the instructions to deploy


Use:
1. Recommended to create a virtual-env
     ```
     pip install virtualenv
     cd my-project/
     virtualenv venv
     source venv/bin/activate
     # venv\Scripts\activate.bat on Windows
     ```
2. Install requirements.txt dependencies
     ```
     pip install -r requirements.txt
     ```
3. Add your AWS credentials to environment variables
     1. Create a profile in `~/.aws/config`
         ```
         [profile my_aws_profile]
         aws_access_key_id = AK...
         aws_secret_access_key = sl...
         region = us-east-1
         ```
     1. Add to environment: `export AWS_PROFILE=my_aws_profile` or add to your `.bashrc` if you like
     persist the variable to other sessions
     1. Run the Python script `put_records_in_kinesis.py`
    
Your event stream is now sent to Kinesis, and from there persisted to S3.