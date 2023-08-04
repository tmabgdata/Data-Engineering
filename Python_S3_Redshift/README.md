# Projeto Python, Amazon S3 e Amazon Redshift

Este é um projeto de demonstração que ilustra como carregar dados de vendas em um Data Lake na Amazon S3 e criar tabelas particionadas no Amazon Redshift usando Python e SQL.

## Estrutura do Projeto

```
Python_S3_Redshift/
│
├── data/
│   ├── sales.csv
│
├── scripts/
│   ├── upload_to_s3.py
│   ├── create_and_load_to_s3.sql
│
└── README.md
```

## Como Usar

1. **Preparação dos Dados:**
   - Coloque seus dados de vendas no arquivo `sales.csv` na pasta `data`.

2. **Upload para o Amazon S3:**
   - Abra o terminal no Visual Studio Code.
   - Navegue até a pasta `scripts`.
   - Execute o script Python para enviar o arquivo para o Amazon S3:
     ```
     python upload_to_s3.py
     ```

3. **Configurando o Amazon Redshift:**
   - Acesse o console do Amazon Redshift e crie um cluster.
   - Abra o editor SQL no console do Amazon Redshift.

4. **Criando Tabelas Particionadas:**
   - No editor SQL, execute os comandos do arquivo `create_and_load_to_s3.sql` para criar as tabelas particionadas no Amazon Redshift.

5. **Carregando Dados nas Tabelas Particionadas:**
   - No editor SQL do Amazon Redshift, execute os comandos `COPY` para carregar os dados das partições do Amazon S3 nas tabelas correspondentes.

6. **Carregando Dados no Data Lake S3:**
   - No editor SQL do Amazon Redshift, execute os comandos `UNLOAD` para carregar os dados das partições no Amazon S3 nas tabelas correspondentes.


## Estrutura do Projeto após a execução

```
Python_S3_Redshift/
│
├── data/
│   ├── sales.csv
    ├── sales_by_region
        ├── sales_eu.csv
        ├── sales_us.csv
│   ├── sales_by_time
        ├── sales_by_time.csv
├── scripts/
│   ├── upload_to_s3.py
│   ├── create_and_load_to_s3.sql
│
└── README.md
```

## Notas

- Certifique-se de ter as credenciais de acesso da AWS configuradas corretamente no seu ambiente.
- Substitua informações como 'seu-bucket-aqui', 'MY_ACCESS_KEY_ID' e 'MY_SECRET_ACCESS_KEY' com os valores reais.

---

Este é um projeto de demonstração e pode ser adaptado para atender a requisitos específicos. Certifique-se de consultar a documentação oficial da AWS para obter informações detalhadas sobre como usar os serviços.