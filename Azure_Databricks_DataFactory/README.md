# Azure Databricks and Data Factory: Creating and Orchestrating Pipelines

<p align="center">
  <img src="https://res.cloudinary.com/dof97idbn/image/upload/v1736911841/real_state_de.jpg" alt="Pipeline de dados imobiliário" width="600" />
</p>

## Project Overview

We, as data engineers for a real estate company, have been tasked with developing a complete data engineering pipeline. Our goal is to:

- Create a Data Lake.
- Ingest real estate data into the inbound layer of the Data Lake.
- Apply data transformations through the Bronze and Silver layers.
- Ensure the pipeline executes automatically at regular intervals (every hour) to keep data consistently updated and processed.

## Tools Used
The project utilizes the following tools and platforms:

- **Azure Cloud Platform**: For resource management and data storage.
- **Azure Data Lake Gen 2**: To create and organize the Data Lake.
- **Azure Data Factory**: For pipeline orchestration and scheduling.
- **Databricks**: To develop and execute data transformation notebooks.
- **Scala**: For data manipulation and transformation.

These tools together form a robust cloud-based data engineering solution.

## Dataset
The provided dataset contains information about real estate prices in Rio de Janeiro and serves as the primary source for analysis and processing.

- Dataset link: [`dataset_imoveis_bruto.json`](https://caelum-online-public.s3.amazonaws.com/2655-databricks-data-factory-pipelines/dados_brutos_imoveis.zip)

## Workflow
The project follows these key steps:

### 1. Azure Account Setup
- Create an Azure account.
- Set up a spending alert to monitor costs.
- Create a resource group for managing project resources.

### 2. Data Lake Creation
- Create a dedicated Azure Storage Account to serve as the Data Lake.
- Structure the Data Lake into the following layers:
  - **Inbound**: Raw data ingestion.
  - **Bronze**: Initial transformations and cleaning.
  - **Silver**: Structuring and further processing.

### 3. Application Registration
- Register an application in Azure to authenticate and authorize interactions with Azure resources.
- Configure permissions for the application using Identity and Access Management (IAM) and Access Control Lists (ACL).

### 4. Databricks Workspace
- Create a Databricks workspace within Azure.
- Configure the connection between Databricks and the Data Lake using the application credentials.
- Mount the Data Lake in Databricks for data access.

### 5. Data Transformations
- **Bronze Layer**:
  - Remove irrelevant data (e.g., images, user information).
  - Add a unique identifier for each property using the `id` field.
  - Save data in Delta format.

- **Silver Layer**:
  - Convert JSON fields into individual columns.
  - Remove unnecessary columns, such as property characteristics.
  - Save data in Delta format.

### 6. Automation and Orchestration
- Use Azure Data Factory to automate the execution of Databricks notebooks.
- Create a pipeline in Azure Data Factory to sequence activities and tasks.
- Configure triggers to execute the pipeline hourly when new data is available.

### 7. Testing and Validation
- Conduct thorough tests to ensure the pipeline executes correctly and integrates seamlessly with other tools.
- Verify data processing accuracy and the functionality of scheduled triggers.

## Project Management
This project was managed using a Trello board. Each task and its progress can be tracked here:

[Trello Board: Databricks and Data Factory Pipeline Project](https://trello.com/b/tjJVN0DS/databricks-e-data-factory-criando-e-orquestrando-pipelines)

## Additional Notes
- Permissions for Data Lake containers were set up using IAM and ACL.
- Data in the Bronze and Silver layers are saved in Delta format for efficient processing.
- Triggers in Azure Data Factory ensure the pipeline executes automatically every hour.

## Repository Structure
```
azure-databricks-datafactory/
├── factory/                       # Azure Data Factory components
│   ├── tmapropertypipeline.json   # Main pipeline configuration
├── linkedService/                 # Linked services for ADF
│   ├── databricks_datafactory_link.json
├── notebooks/                     # Databricks notebooks for transformations
│   ├── Bronze_to_Silver.scala     # Transform Bronze data to Silver
│   ├── Inbound_to_Bronze.scala    # Transform Inbound data to Bronze
├── pipeline/                      # Azure Data Factory pipeline definitions
│   ├── datalake-ingestion.json    # Pipeline for data lake ingestion
├── tmapropertypipeline/           # ARM templates for the pipeline
│   ├── globalParameters/
│   ├── linkedTemplates/
│   ├── ARMTemplateForFactory.json
│   ├── ARMTemplateParametersForFactory.json
├── trigger/                       # Pipeline triggers
│   ├── pipeline_trigger.json
├── dataset/                       # Real estate dataset
│   ├── dataset_imoveis_bruto.json
├── .gitignore                     # Git ignore rules
├── README.md                      # Project overview (this file)
├── publish_config.json            # Publishing configuration
```

## Notebooks
The notebooks folder contains the Scala code used for data transformations. Refer to:
- `Inbound_to_Bronze.scala`: Processes raw data into the Bronze layer.
- `Bronze_to_Silver.scala`: Refines Bronze data into the Silver layer.

Please navigate to the `notebooks/` directory to view and execute the code.

## How to Get Started
1. Clone the repository:
   ```bash
   git clone https://github.com/tmabgdata/azure-databricks-datafactory.git
   ```
2. Follow the steps in the workflow section to set up the required Azure resources.
3. Refer to the `notebooks` folder for Databricks transformation code.
4. Use the `pipeline` and `factory` folders to import pipeline definitions into Azure Data Factory.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For further information or inquiries, please contact:

**Thiago Alves**  
[GitHub](https://github.com/tmabgdata)
