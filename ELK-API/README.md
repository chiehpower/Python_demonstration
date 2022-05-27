# ELK with Python API

1. We will use loguru instead of logging.
    please check this file [loguru_to_elk.py](./loguru_to_elk.py)
2. Our goal is to retrieve the data from ES.
    please check this file [retrieve-1.py](./retrieve-1.py)
3. Write the data into ES directly. Not using log way.


# Troubleshooting
1. import problem
    ```
    Traceback (most recent call last):
      File "loguru_to_elk.py", line 1, in <module>
        from cmreslogging.handlers import CMRESHandler
      File "/home/chieh/.local/lib/python3.6/site-packages/cmreslogging/handlers.py", line 10, in <module>
        from elasticsearch import Elasticsearch, RequestsHttpConnection
    ImportError: cannot import name 'RequestsHttpConnection'
    ```

    Solution:
    
    Downgrade the es version by 
    
    ```
    python3 -m pip install --no-cache-dir elasticsearch==7.13.4
    python3 -m pip install --no-cache-dir elastic-transport==8.0.1
    ```