def errors_only(record):
    if record["level"].name != "ERROR":
        return False
    return True


from loguru import logger
import os

logger.add(
    os.path.join(os.getcwd(), "python.log"),
    rotation="10 days",
    encoding="utf-8",
    enqueue=True,
    format="{time} {level} {message}",
    filter=errors_only,
    level="INFO",
)

from cmreslogging.handlers import CMRESHandler
handler = CMRESHandler(hosts=[{'host': '10.1.2.102', 'port': 5000}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="logstash-*")

# logger.add("1.log")
logger.add(handler)

for i in range(10):
    logger.debug(f'From loguru, it is no. {i} writing...')

# @logger.catch
# def t(a):
#     print(a)

# t(100000123123123)

### To retrieve the data
import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import time 

Start = time.time()
hosts = ['10.1.2.102:9200']
es = Elasticsearch(hosts=hosts)
# print(es.info())

searchBody = {
    "sort" : [
        { "@timestamp" : {"order" : "desc"}}
    ],
    "query" : {
        "bool": {
          "must": {
              "match": { 
                  "host": "10.1.2.84" 
              }
          }
        }        
    }
}

response = es.search(
    index="logstash-*",body=searchBody)

A = response["hits"]["hits"]

for i in A:
    print(i)
    print("---")

print("time:", time.time() - Start)