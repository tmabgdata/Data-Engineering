// Databricks notebook source
// MAGIC %md
// MAGIC To store the data in the bronze layer, we will perform some initial transformations based on what is most relevant for the teams that will use this data:
// MAGIC
// MAGIC - Remove information not relevant to the company, such as images or users of real estate;
// MAGIC
// MAGIC - Ensure the presence of a unique identification column for each property, using the "id" field.
// MAGIC
// MAGIC The data must be saved in the bronze layer in delta format.

// COMMAND ----------

// MAGIC %python
// MAGIC #checking data
// MAGIC dbutils.fs.ls("/mnt/data/inbound")

// COMMAND ----------

// read inbound data
val path = "dbfs:/mnt/data/inbound/dados_brutos_imoveis.json"
val data = spark.read.json(path)

// COMMAND ----------

display(data)

// COMMAND ----------

// remove cols
val ads_data = data.drop("imagens", "usuario")
display(ads_data)

// COMMAND ----------

// creating col id by user id
import org.apache.spark.sql.functions.col
val df_bronze = ads_data.withColumn("id", col("anuncio.id"))
display(df_bronze)

// COMMAND ----------

// saving data to bronze layer
val path = "dbfs:/mnt/data/bronze/property_dataset"
df_bronze.write.format("delta").mode(SaveMode.Overwrite).save(path)
