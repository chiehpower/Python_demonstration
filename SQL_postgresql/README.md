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
    ```
    psql -U admin -w admin -a -f insert_values.sql
    ```

3. Get values and filtered by time.
    ```
    psql -U admin -w admin -a -f get_values_by_time.sql
    ```
    Output:
    ```
    root@e0a374a289e5:~/test# psql -U admin -w admin -a -f get_values_by_time.sql

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
    ```
    