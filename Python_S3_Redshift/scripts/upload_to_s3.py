import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name = 'sa-east-1',
    aws_access_key_id = '<-- Key ID -->',
    aws_secret_access_key = '<-- Secret Key -->'
    )

s3.meta.client.upload_file('/content/sales.csv', 'seu-bucket-aqui', 'sales/sales.csv')

print('Arquivo enviado para o Amazon S3 com sucesso!')