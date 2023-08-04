-- Criando tabela de vendas particionada por região no Amazon Redshift
CREATE TABLE sales_by_region (
    sale_id INT,
    product_name VARCHAR(255),
    sale_date DATE,
    region VARCHAR(50)
) DISTKEY (region) SORTKEY (sale_date);

-- Carregando dados na tabela particionada por região
COPY sales_by_region FROM 's3://seu-bucket/sales/sales.csv'
CREDENTIALS 'aws_access_key_id=<- Key ID ->;aws_secret_access_key=<- Access Key ->'
CSV
IGNOREHEADER 1;

-- Criando tabela de vendas particionada por tempo no Amazon Redshift
CREATE TABLE sales_by_time (
    sale_id INT,
    product_name VARCHAR(255),
    sale_date DATE,
    region VARCHAR(50)
) DISTKEY (sale_date) SORTKEY (sale_date);

-- Carregando dados na tabela particionada por tempo
COPY sales_by_time FROM 's3://seu-bucket/sales/sales.csv' 
CREDENTIALS 'aws_access_key_id=<- Key ID ->;aws_secret_access_key=<- Access Key ->'
CSV
IGNOREHEADER 1;

-- Região US
UNLOAD ('SELECT * FROM sales_by_region
    WHERE region = ''US'' ')
TO 's3://seu-bucket/sales/sales_by_region/sales_us.csv'
CREDENTIALS 'aws_access_key_id=<- Key ID ->;aws_secret_access_key=<- Access Key ->'
DELIMITER ','
ADDQUOTES
ALLOWOVERWRITE
PARALLEL OFF;

--Região EU
UNLOAD ('SELECT * FROM sales_by_region
    WHERE region = ''EU'' ')
TO 's3://seu-bucket/sales/sales_by_region/sales_eu.csv'
CREDENTIALS 'aws_access_key_id=<- Key ID ->;aws_secret_access_key=<- Access Key ->'
DELIMITER ','
ADDQUOTES
ALLOWOVERWRITE
PARALLEL OFF;

-- Carregar dados da tabela particionada por tempo para o Amazon S3
UNLOAD ('SELECT * FROM sales_by_time')
TO 's3://seu-bucket/sales/sales_by_time/sales_by_time.csv'
CREDENTIALS 'aws_access_key_id=<- Key ID ->;aws_secret_access_key=<- Access Key ->'
DELIMITER ','
ADDQUOTES
ALLOWOVERWRITE
PARALLEL OFF;