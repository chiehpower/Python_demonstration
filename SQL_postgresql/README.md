# About PostgreSQL Database

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
