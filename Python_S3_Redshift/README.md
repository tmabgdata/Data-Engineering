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
│   ├── create_redshift_tables.sql
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
   - No editor SQL, execute os comandos dos arquivos `create_redshift_region_tables.sql` e `create_redshift_time_tables` para criar as tabelas particionadas no Amazon Redshift.

5. **Carregando Dados nas Tabelas Particionadas:**
   - No editor SQL do Amazon Redshift, execute os comandos `COPY` para carregar os dados das partições do Amazon S3 nas tabelas correspondentes.

6. **Executando Consultas Analíticas:**
   - Utilize o editor SQL do Amazon Redshift para executar consultas nas tabelas particionadas e observe o desempenho.

## Notas

- Certifique-se de ter as credenciais de acesso da AWS configuradas corretamente no seu ambiente.
- Substitua informações como 'seu-bucket-aqui', 'MY_ACCESS_KEY_ID' e 'MY_SECRET_ACCESS_KEY' com os valores reais.

---

Este é um projeto de demonstração e pode ser adaptado para atender a requisitos específicos. Certifique-se de consultar a documentação oficial da AWS para obter informações detalhadas sobre como usar os serviços.