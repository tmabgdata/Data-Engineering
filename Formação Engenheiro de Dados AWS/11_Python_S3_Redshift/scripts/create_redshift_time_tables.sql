-- SQL - Criando tabela particionada por mês e ano no Amazon Redshift
CREATE TABLE sales_time (
    sale_id INT,
    product_name VARCHAR(255),
    sale_date DATE
) DISTKEY (sale_date) SORTKEY (sale_date)
PARTITION BY RANGE (EXTRACT(YEAR FROM sale_date), EXTRACT(MONTH FROM sale_date));

-- Carregando partições
COPY sales_time FROM 's3://meu-data-lake/sales/sales.csv' 
CREDENTIALS 'aws_access_key_id=MY_ACCESS_KEY_ID;aws_secret_access_key=MY_SECRET_ACCESS_KEY'
CSV;
