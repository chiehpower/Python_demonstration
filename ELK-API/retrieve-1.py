### First stage.
## Codes referenced from: https://github.com/twtrubiks/docker-elk-tutorial/blob/master/python-logging/demo_logging.py
import logging
import logstash
import sys

# host = '0.0.0.0'
host = '10.1.2.102'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
# TCP
test_logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra)
print('done,please see kibana')

### Second stage.
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