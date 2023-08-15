# Simulated MongoDB Project Documentation

This documentation provides an overview of a simulated MongoDB project conducted in Google Colab using the `mongomock` library. The purpose of this project is to demonstrate how to interact with a MongoDB-like environment for learning and testing purposes.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
    - [Install the Required Libraries](#install-the-required-libraries)
    - [Create a Simulated MongoDB Environment](#create-a-simulated-mongodb-environment)
3. [Data Insertion](#data-insertion)
4. [Query and Operation Examples](#query-and-operation-examples)
    - [Basic Query: Find All Documents](#basic-query-find-all-documents)
    - [Query with Criteria: Find Documents by Age](#query-with-criteria-find-documents-by-age)
    - [Query with Range: Find Documents by Age Range](#query-with-range-find-documents-by-age-range)
    - [Query with Inclusion: Find Documents by City](#query-with-inclusion-find-documents-by-city)
    - [Update Documents: Update Status](#update-documents-update-status)
    - [Delete Documents: Delete by Age](#delete-documents-delete-by-age)
    - [Count Documents: Count Total Documents](#count-documents-count-total-documents)
    - [Find Youngest Person](#find-youngest-person)
    - [Find Oldest Person in a City](#find-oldest-person-in-a-city)
    - [Calculate Average Age](#calculate-average-age)
    - [Find Distinct Cities](#find-distinct-cities)
5. [Conclusion](#conclusion)
6. [References](#references)

## Introduction

This project demonstrates how to work with a simulated MongoDB environment using the `mongomock` library within Google Colab. The environment emulates the MongoDB interface while storing data in memory, making it ideal for learning and experimentation without the need for an external MongoDB server.

## Setup

### Install the Required Libraries

In the first code cell of the notebook, install the `mongomock` library to create a simulated MongoDB environment.

```python
!pip install mongomock
!pip install pymongo
```

### Create a Simulated MongoDB Environment

The following code cell demonstrates how to import the `mongomock` library, create a simulated MongoDB client, and establish a connection to a simulated database and collection.

```python
import mongomock

# Create a simulated MongoDB client and database
simulated_client = mongomock.MongoClient()
simulated_db = simulated_client["mydatabase"]
simulated_collection = simulated_db["mycollection"]
```

## Data Insertion

In the data insertion section, populate the simulated collection with sample data using the `insert_one` method.

```python
data = [
    # ... sample data ...
]

# Insert the documents into the simulated collection
for doc in data:
    simulated_collection.insert_one(doc)

print("Documents inserted:", len(data))
```

## Query and Operation Examples

This section demonstrates various MongoDB-like queries and operations in the simulated environment.

### Basic Query: Find All Documents

```python
result = simulated_collection.find()
for doc in result:
    print(doc)
```

### Query with Criteria: Find Documents by Age

```python
query = {"age": {"$gt": 30}}
result = simulated_collection.find(query)
for doc in result:
    print(doc)
```

### Query with Range: Find Documents by Age Range

```python
query = {"age": {"$gte": 25, "$lte": 30}}
result = simulated_collection.find(query)
for doc in result:
    print(doc)
```

### Query with Inclusion: Find Documents by City

```python
cities_to_find = ["New York", "Los Angeles", "Chicago"]
query = {"city": {"$in": cities_to_find}}
result = simulated_collection.find(query)
for doc in result:
    print(doc)
```

### Update Documents: Update Status

```python
query = {"age": {"$gt": 30}}
new_values = {"$set": {"status": "Senior"}}
updated_count = simulated_collection.update_many(query, new_values)
print(f"Updated {updated_count.modified_count} documents.")
```

### Delete Documents: Delete by Age

```python
query = {"age": {"$lt": 25}}
deleted_count = simulated_collection.delete_many(query)
print(f"Deleted {deleted_count.deleted_count} documents.")
```

## Count Documents: Count Total Documents

```python
doc_count = simulated_collection.count_documents({})
print("Total documents:", doc_count)
```

### Find Youngest Person

```python
youngest_person = simulated_collection.find_one({}, sort=[("age", pymongo.ASCENDING)])
print("Youngest person:", youngest_person)
```

### Find Oldest Person in a City

```python
oldest_person_city = "San Francisco"
query = {"city": oldest_person_city}
oldest_person = simulated_collection.find_one(query, sort=[("age", pymongo.DESCENDING)])
print(f"Oldest person in {oldest_person_city}:", oldest_person)
```

### Calculate Average Age

```python
average_age_result = simulated_collection.aggregate([
    {"$group": {"_id": None, "average_age": {"$avg": "$age"}}}
])
average_age = list(average_age_result)[0]["average_age"]
print("Average age:", round(average_age, 2))
```

### Find Distinct Cities

```python
distinct_cities = simulated_collection.distinct("city")
distinct_cities.sort()
print("Distinct cities:", distinct_cities)
```

## Conclusion

This documentation provided an overview of how to create and interact with a simulated MongoDB environment using the `mongomock` library in Google Colab. You've learned how to perform basic and advanced queries, insert and manipulate data, and conduct various operations similar to those in a real MongoDB environment.

## References

- `mongomock` GitHub Repository: [https://github.com/mongomock/mongomock](https://github.com/mongomock/mongomock)
- MongoDB Documentation: [https://docs.mongodb.com/](https://docs.mongodb.com/)
```