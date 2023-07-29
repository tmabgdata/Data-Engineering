import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node clientes
clientes_node1690576250780 = glueContext.create_dynamic_frame.from_catalog(
    database="tmabigdatadbglue",
    table_name="clientes_csv",
    transformation_ctx="clientes_node1690576250780",
)

# Script generated for node vendas
vendas_node1690574864780 = glueContext.create_dynamic_frame.from_catalog(
    database="tmabigdatadbglue",
    table_name="vendas_csv",
    transformation_ctx="vendas_node1690574864780",
)

# Script generated for node itensvendas
itensvendas_node1690575484725 = glueContext.create_dynamic_frame.from_catalog(
    database="tmabigdatadbglue",
    table_name="itensvenda_csv",
    transformation_ctx="itensvendas_node1690575484725",
)

# Script generated for node produtos
produtos_node1690576480361 = glueContext.create_dynamic_frame.from_catalog(
    database="tmabigdatadbglue",
    table_name="produtos_csv",
    transformation_ctx="produtos_node1690576480361",
)

# Script generated for node vendedores
vendedores_node1690576891818 = glueContext.create_dynamic_frame.from_catalog(
    database="tmabigdatadbglue",
    table_name="vendedores_csv",
    transformation_ctx="vendedores_node1690576891818",
)

# Script generated for node vendas_mapping
vendas_mapping_node1690575211407 = ApplyMapping.apply(
    frame=vendas_node1690574864780,
    mappings=[
        ("idvenda", "long", "idvenda", "long"),
        ("idvendedor", "long", "idvendedor_vendas", "long"),
        ("idcliente", "long", "idcliente_vendas", "long"),
        ("data", "string", "data", "string"),
        ("total", "double", "total", "double"),
    ],
    transformation_ctx="vendas_mapping_node1690575211407",
)

# Script generated for node itensvendas_mapping
itensvendas_mapping_node1690575510466 = ApplyMapping.apply(
    frame=itensvendas_node1690575484725,
    mappings=[
        ("idproduto", "long", "idproduto_itensvendas", "long"),
        ("idvenda", "long", "idvenda_itensvendas", "long"),
        ("quantidade", "long", "quantidade", "long"),
        ("valorunitario", "double", "valorunitario", "double"),
        ("valortotal", "double", "valortotal", "double"),
        ("desconto", "double", "desconto", "double"),
    ],
    transformation_ctx="itensvendas_mapping_node1690575510466",
)

# Script generated for node vendas_itensvendas
vendas_itensvendas_node1690575734078 = Join.apply(
    frame1=vendas_mapping_node1690575211407,
    frame2=itensvendas_mapping_node1690575510466,
    keys1=["idvenda"],
    keys2=["idvenda_itensvendas"],
    transformation_ctx="vendas_itensvendas_node1690575734078",
)

# Script generated for node join_clientes
join_clientes_node1690576397538 = Join.apply(
    frame1=clientes_node1690576250780,
    frame2=vendas_itensvendas_node1690575734078,
    keys1=["idcliente"],
    keys2=["idcliente_vendas"],
    transformation_ctx="join_clientes_node1690576397538",
)

# Script generated for node join_produtos
join_produtos_node1690576659791 = Join.apply(
    frame1=produtos_node1690576480361,
    frame2=join_clientes_node1690576397538,
    keys1=["idproduto"],
    keys2=["idproduto_itensvendas"],
    transformation_ctx="join_produtos_node1690576659791",
)

# Script generated for node join_vendedores
join_vendedores_node1690576905537 = Join.apply(
    frame1=vendedores_node1690576891818,
    frame2=join_produtos_node1690576659791,
    keys1=["idvendedor"],
    keys2=["idvendedor_vendas"],
    transformation_ctx="join_vendedores_node1690576905537",
)

# Script generated for node colunas_finais
colunas_finais_node1690577090747 = ApplyMapping.apply(
    frame=join_vendedores_node1690576905537,
    mappings=[
        ("nome", "string", "nome", "string"),
        ("produto", "string", "produto", "string"),
        ("preco", "double", "preco", "double"),
        ("cliente", "string", "cliente", "string"),
        ("estado", "string", "estado", "string"),
        ("sexo", "string", "sexo", "string"),
        ("status", "string", "status", "string"),
        ("data", "string", "data", "string"),
        ("total", "double", "total", "double"),
        ("quantidade", "long", "quantidade", "long"),
        ("valorunitario", "double", "valorunitario", "double"),
        ("valortotal", "double", "valortotal", "double"),
        ("desconto", "double", "desconto", "double"),
    ],
    transformation_ctx="colunas_finais_node1690577090747",
)

# Script generated for node datalake
datalake_node1690577275510 = glueContext.write_dynamic_frame.from_options(
    frame=colunas_finais_node1690577090747,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://tmabigdataglue/datalake/",
        "partitionKeys": ["status"],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="datalake_node1690577275510",
)

job.commit()
