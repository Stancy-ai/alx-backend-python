# Python Generators

This repository contains practical exercises on Python generators, focusing on memory-efficient data processing using real SQL data pipelines, aligned with ALX backend professional development standards.


##  What You Will Learn

How to build and use generators to:

1. Stream SQL rows efficiently.
2. Process data in batches without loading the entire dataset into memory.
3. Implement lazy pagination for scalable data retrieval.
4. Compute aggregates (e.g., average age) without SQL aggregation functions, ensuring algorithmic mastery.

 Using yield for clean, readable, and scalable pipelines in backend workflows.

Applying generators to real-world scenarios such as:

1. User data streaming
2. Batch processing
3. Pagination
4. Memory-efficient analytics


## Exercises Overview

### `0-stream_users.py`

Streams user rows one by one from the `user_data` SQL table using a generator.

### `1-batch_processing.py`

Fetches rows in batches using a generator, then filters users over the age of 25 while maintaining low memory usage.

###  `2-lazy_paginate.py`

Implements lazy pagination, fetching only the next page from the database when needed using a generator.

### `3-average_age.py`

Uses a generator to compute the average age** of users without loading the entire dataset into memory, without using SQL `AVG()`.


## Requirements

1. Python 3.8+
2. `mysql-connector-python` installed
3. Access to the `ALX_prodev` MySQL database with a populated `user_data` table.
4. Environment variables for database credentials if needed.

## Usage

Activate your environment and run any script:

```bash
export MYSQL_USER=root
export MYSQL_PASSWORD=mysecret
pip install mysql-connector-python
python 0-main.py         
```



