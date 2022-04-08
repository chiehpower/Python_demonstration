#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Chieh
"""
# import the connect library from psycopg2
from psycopg2 import connect

class PostgreSQLDB(object):
    def __init__(self, host, port='5432', user='admin', password='admin', dbname='admin'):
        """
            dbname = "admin",
            user = "admin",
            password = "admin",
            host = "172.28.1.4",
            port = "5432"
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname

    def execute_action(self, sql):
        conn = connect(
            dbname=self.dbname,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
            )

        cur = conn.cursor()
        try:
            cur.execute(sql)
        except:
            conn.close()
            return False
        conn.commit()
        conn.close()
        return True

    def create_table(self, table_name):
        table_name = table_name.lower()
        
        all_tables = self.get_tables()
        print(table_name, all_tables)
        if table_name in all_tables:
            print("Already existed.")
            return False
        # create a table
        sql = """
            CREATE TABLE {} (
                id serial PRIMARY KEY,
                name varchar(100) NOT NULL
            );
            """.format(table_name)

        res = self.execute_action(sql)
        if res:
            return True
        else:
            return False
    
    def get_tables(self):
        conn = connect(
            dbname=self.dbname,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
            )
        cur = conn.cursor()
        cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
        all_tables = []
        for table in cur.fetchall():
            all_tables.append(table[0])
        conn.close()
        return all_tables

    def InsertOneRowIntoTable(self, table_name, key, value):
        sql = """INSERT INTO {} {} VALUES {}""".format(table_name, key, value)
        
        res = self.execute_action(sql)
        if res:
            return True
        else:
            return False

    def GetValueFromTable(self, table_name):
        conn = connect(
            dbname=self.dbname,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
            )
        cur = conn.cursor()
        cur.execute("""SELECT * FROM {}""".format(table_name))
        all_tables = []
        for table in cur.fetchall():
            all_tables.append(table)
        conn.close()
        return all_tables

    def DeleteValueFromTable(self, table_name, key):
        sql = """DELETE FROM {} WHERE {}""".format(table_name, key)
        res = self.execute_action(sql)
        if res:
            return True
        else:
            return False


if __name__ == "__main__":

    dbname = "admin"
    user = "admin"
    password = "admin"
    host = "172.28.1.4"
    port = "5432"

    table_name = "Password"

    PostgreSQL = PostgreSQLDB(host, port, user, password, dbname)

    res = PostgreSQL.create_table(table_name)
    print(res)

    res = PostgreSQL.InsertOneRowIntoTable(table_name, "(id, name)", "(1, 'test123456')")
    print(res)
    
    # res = PostgreSQL.get_tables()

    res = PostgreSQL.GetValueFromTable(table_name)

    print(res)
    
    for i in res:
        print(i, i[0])
        key_ = 1
        if i[0] == key_:
            res = PostgreSQL.DeleteValueFromTable(table_name, f"id = {key_}")
            print("Done")
            print(res)
            break
