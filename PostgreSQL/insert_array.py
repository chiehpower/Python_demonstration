#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Chieh
"""
# import the connect library from psycopg2
# from psycopg2 import connect
import psycopg2 as psy
import numpy as np
import pickle
import time

if __name__ == "__main__":

    dbname = "admin"
    user = "admin"
    password = "admin"
    host = "10.1.2.84"
    port = "5432"

    # table_name = "numpy_arrays"
    # conn = connect(
    #         dbname=dbname,
    #         host=host,
    #         port=port,
    #         user=user,
    #         password=password
    #         )

    # cur = conn.cursor()

    #### -----------
    db_connect_kwargs = {
        'dbname': dbname,
        'user': user,
        'password': password,
        'host': host,
        'port': port
    }

    connection = psy.connect(**db_connect_kwargs)
    connection.set_session(autocommit=True)
    cursor = connection.cursor()

    cursor.execute(
        """
        DROP TABLE IF EXISTS numpy_arrays;
        CREATE TABLE numpy_arrays (
            uuid VARCHAR PRIMARY KEY,
            patch BYTEA,
            scale BYTEA
        )
        """
    )
    # #### -----------

    # some_array = np.random.rand(1500,550)
    # print(some_array.shape)
    some_array_uuid = 'some_array'

    testdummypatch = np.random.rand(27, 1, 256).astype(np.float32)
    testdummyscale = np.random.randint(1, 4, (1,27)).astype(np.int32)

    res = cursor.execute(
        """
        INSERT INTO numpy_arrays(uuid, patch, scale)
        VALUES (%s, %s, %s)
        """,
        (some_array_uuid, pickle.dumps(testdummypatch), pickle.dumps(testdummyscale))
    )

    print(res)
    print("---")
    uuid = 'some_array'
    for i in range(1):
        lt = time.time()
        cursor.execute(
            """
            SELECT patch
            FROM numpy_arrays
            WHERE uuid=%s
            """,
            (uuid,)
        )
        patch = pickle.loads(cursor.fetchone()[0])
        print(patch)
        cursor.execute(
            """
            SELECT scale
            FROM numpy_arrays
            WHERE uuid=%s
            """,
            (uuid,)
        )
        scale = pickle.loads(cursor.fetchone()[0])
        print(scale)
        print("Take : {}".format(time.time()-lt))
    print("---")
    print(type(patch))