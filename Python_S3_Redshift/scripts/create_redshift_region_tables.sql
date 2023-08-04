-- SQL - Criando tabela particionada por região no Amazon Redshift
CREATE TABLE sales (
    sale_id INT,
    product_name VARCHAR(255),
    sale_date DATE,
    region VARCHAR(50)
) DISTKEY (region) SORTKEY (sale_date)
PARTITION BY LIST (region);

-- Carregando partições
COPY sales FROM 's3://meu-data-lake/sales/sales.csv' 
CREDENTIALS 'aws_access_key_id=MY_ACCESS_KEY_ID;aws_secret_access_key=MY_SECRET_ACCESS_KEY'
CSV;
