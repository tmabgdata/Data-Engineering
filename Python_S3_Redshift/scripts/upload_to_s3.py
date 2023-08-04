import boto3

s3 = boto3.client('s3')
bucket_name = 'seu-bucket-aqui'  # Substitua pelo nome real do seu bucket

file_name = 'data/sales.csv'  # Caminho para o arquivo de dados

# Faz o upload do arquivo para o S3
s3.upload_file(file_name, bucket_name, 'sales/sales.csv')

print('Arquivo enviado para o Amazon S3 com sucesso!')
