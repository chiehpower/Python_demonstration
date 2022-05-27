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