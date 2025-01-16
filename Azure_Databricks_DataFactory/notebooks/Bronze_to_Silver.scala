// Databricks notebook source
// MAGIC %md
// MAGIC In this step, we will read the data on the bronze layer and apply transformations to structure them properly before saving them on the silver layer. The transformations will include:
// MAGIC
// MAGIC - Convert each JSON field into an individual column.
// MAGIC
// MAGIC - Remove column(s) containing information about the characteristics of the real estate, as they are not necessary for this phase.
// MAGIC
// MAGIC Data should be saved in the silver layer in delta format.

// COMMAND ----------

// MAGIC %python
// MAGIC # checking bronze directory
// MAGIC dbutils.fs.ls("mnt/data/bronze/")

// COMMAND ----------

// read data in bronze layer
val path = "/mnt/data/bronze/property_dataset"
val df = spark.read.format("delta").load(path)

// COMMAND ----------

display(df)

// COMMAND ----------

// jason fields to columns
display(df.select("anuncio.*"))

// COMMAND ----------

// jason sub-fields to columns
display(
  df.select("anuncio.*", "anuncio.endereco.*")
)

// COMMAND ----------

// detailed data
val detailed_data = df.select("anuncio.*", "anuncio.endereco.*")

// COMMAND ----------

display(detailed_data)

// COMMAND ----------

// remove cols
val df_silver = detailed_data.drop("caracteristicas", "endereco")
display(df_silver)

// COMMAND ----------

// saving in silver layer
val path = "dbfs:/mnt/data/silver/property_dataset"
df_silver.write.format("delta").mode("overwrite").save(path)
