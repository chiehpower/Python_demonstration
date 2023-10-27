# Use python to access PostgreSQL database

Chec[here](https://chieh.us/docs/PostgreSQL/basic-commands)
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

# Login the DB directly

```
docker exec -ti db bash
psql -U admin
SELECT * FROM Password; 
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

---

# About the PostgreSQL database for pure SQL programming

## Docker

Start the database server
    ```
    docker-compose up -d
    ```

## Manage the DB tables

1. Create tables

    ```
    cd /root/test/
    psql -U admin -w admin -a -f create_table.sql
    ```

    Check the table in the DB.

    ```
    $ psql -U admin -w admin 
    $ \dt
    
    List of relations

    Schema |   Name   | Type  | Owner
    --------+----------+-------+-------
    public | projects | table | admin
    public | users    | table | admin
    (2 rows)
    ```

2. Insert values into the table.

    ```
    psql -U admin -w admin -a -f insert_values.sql
    ```

3. Get values and filtered by time.

    ```
    psql -U admin -w admin -a -f get_values_by_time.sql
    ```

    Output:

    ```
    SELECT * FROM users
    WHERE created >= '2023-10-26 00:00:00' AND created <= '2023-10-27 05:00:00';
    user_id | username |          created
    ---------+----------+----------------------------
        1 | user1    | 2023-10-27 03:17:15.000032
    (1 row)

    SELECT * FROM projects
    WHERE created >= '2023-10-30 00:00:00' AND created <= '2023-10-31 00:00:00';
    project_id | project_name |       created       | created_by_user_id
    ------------+--------------+---------------------+--------------------
            1 | Project A    | 2023-10-30 14:45:00 |                  1
    (1 row)

    SELECT users.username, projects.project_name
    FROM users
    JOIN projects ON users.user_id = projects.created_by_user_id
    WHERE projects.created >= '2023-10-30 00:00:00' AND projects.created <= '2023-10-31 00:00:00'
    AND projects.project_name = 'Project A';
    username | project_name
    ----------+--------------
    user1    | Project A
    (1 row)

    SELECT projects.project_name
    FROM projects
    WHERE projects.created >= '2023-10-30 00:00:00' AND projects.created <= '2023-10-31 00:00:00'
    AND projects.project_name = 'Project A';
    project_name
    --------------

    Project A
    (1 row)

    SELECT u.username, p.project_name
    FROM projects p
    JOIN users u ON p.created_by_user_id = u.user_id
    WHERE p.created >= '2023-10-30 00:00:00' AND p.created <= '2023-10-31 00:00:00'
    AND p.project_name = 'Project A'
    AND u.username = 'user1';
    username | project_name
    ----------+--------------
    user1    | Project A
    (1 row)
    ```
