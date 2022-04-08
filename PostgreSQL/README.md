# Use python to access PostgreSQL database

## Goal


We will use docker to launch a PostgreSQL databse, and then we will use python to do the controlling from the PostgreSQL database.

You are able to retrieve data outside of database container.

## Python requirements

```
pip3 install psycopg2
```

## Usage

1. Let's start the database first via docker-compose
    ```
    docker-compose up -d
    ```
2. Run the Python script.
    ```
    python3 main.py
    ```

## Trobuleshooting

1. `PostgreSQL - port 5432 already in use`

Solution:

```
$ sudo lsof -i :5432
$ sudo pkill -u postgres
```

2. `pip install psycopg2 : pg_config executable not found`

Solution:

```
sudo apt-get install libpq-dev
```

## Reference

1. https://www.itread01.com/article/1529892624.html
2. https://kb.objectrocket.com/postgresql/python-and-postgresql-docker-container-part-2-1063