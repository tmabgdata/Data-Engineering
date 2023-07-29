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

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1690590480481 = glueContext.create_dynamic_frame.from_catalog(
    database="tmawindfarm",
    table_name="tmawindfarmdata",
    transformation_ctx="AWSGlueDataCatalog_node1690590480481",
)

# Script generated for node Amazon S3
AmazonS3_node1690590506044 = glueContext.write_dynamic_frame.from_options(
    frame=AWSGlueDataCatalog_node1690590480481,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://tmawindfarmdatalake/datalake/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1690590506044",
)

job.commit()
