# Azure Cloud Data Pipeline

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Microsoft Azure Blob Storage, Python, Pandas, and PostgreSQL.

The pipeline extracts sales data stored in Azure Blob Storage, performs data transformation and validation using Pandas, and loads the processed data into PostgreSQL for further analysis and reporting.

---

## Architecture

```text
Sales CSV File
       ↓
Azure Blob Storage
       ↓
Python Azure SDK
       ↓
Pandas Data Processing
       ↓
PostgreSQL Database
       ↓
SQL Analysis & Validation
```

---

## Technologies Used

* Microsoft Azure Blob Storage
* Python 3
* Pandas
* Azure Storage Blob SDK
* PostgreSQL
* SQLAlchemy
* Git & GitHub

---

## Project Structure

```text
azure-cloud-data-pipeline/
│
├── config/
│   └── config.py
│
├── data/
│   └── processed/
│       └── cleaned_sales_data.csv
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── extract/
│   │   └── blob_reader.py
│   │
│   ├── transform/
│   │   └── data_cleaner.py
│   │
│   ├── load/
│   │   └── postgres_loader.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## ETL Workflow

### Extract

* Connected to Azure Blob Storage using Azure Storage SDK.
* Downloaded sales data from Azure Blob Container.
* Loaded data into a Pandas DataFrame.

### Transform

* Standardized column names.
* Removed duplicate records.
* Generated a new business metric:

  `total_amount = quantity × price`

### Load

* Connected to PostgreSQL using SQLAlchemy.
* Loaded transformed data into the `sales` table.
* Validated loaded records using SQL queries.

---

## Sample SQL Queries

```sql
SELECT * FROM sales;

SELECT SUM(total_amount) AS total_sales
FROM sales;

SELECT city,
       SUM(total_amount) AS revenue
FROM sales
GROUP BY city;
```

---

## Key Features

* Cloud-based data ingestion from Azure Blob Storage
* Automated data transformation using Pandas
* PostgreSQL integration
* Modular ETL architecture
* SQL-based validation
* Version controlled using Git and GitHub

---

## Learning Outcomes

Through this project, the following concepts were implemented and practiced:

* Azure Storage Account Management
* Azure Blob Storage Operations
* Python Data Engineering Workflows
* Pandas Data Processing
* ETL Pipeline Design
* PostgreSQL Database Integration
* SQL Querying and Validation
* Git and GitHub Version Control

---

## Future Enhancements

* Azure Data Factory Integration
* Azure Databricks / PySpark Processing
* Automated Scheduling
* Data Quality Monitoring
* Cloud Data Warehouse Integration

---

## Author

Aakash Pappala

Aspiring Azure Data Engineer | Python | SQL | PostgreSQL | Cloud Data Engineering
