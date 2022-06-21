"""
Before to use this script, please run the send_log.py first.
"""
print("Please use Python 3.8.")
import sys
pythonversion = sys.version
print("Your Python version is: ", pythonversion)
if pythonversion[:3] == '3.6':
    raise 'Cannot use Python 3.6'
from elasticsearch import Elasticsearch
import time
from time import ctime, gmtime, strftime

if __name__ == '__main__':
    # hosts = ['10.1.2.102:9200'] 
    hosts = ['10.1.2.102:9200']
    es = Elasticsearch(hosts=hosts)

    time_ = 50
    index = 'logstash-*'
    # user = 'admin'

    # {
    # "query": {
    #     "match": {
    #     "host": "10.1.2.84"
    #     }
    # }
    # }

    # print("User: ", user, "index:", index, "time:", 10000)
    # searchBody = {
    #     "sort" : [
    #         {"time" : {"order" : "desc"}}
    #     ],
    #     "size": 10000,
    # }

    searchBody =  {
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
    },
    "size": 10000   
    }   

    es.indices.refresh(index)

    response = es.search(
        index=index, body=searchBody)

    collect = {}
    for i in response["hits"]['hits']:

        print("---")
        try:
            new = eval(i['_source']['message'])
            new = eval(new['message'])
        except:
            break
        print(new)
        model_name = new['model_name']
        state_id = new['state_id']
        time_ = new['time']
        user = new['user']
        print("model_name: ", model_name, "| state_id: ", state_id, "| time: ", time_, "| user: ", user)
        
        time_ /= 10000000
        ccc = time.strptime(ctime(time_), "%a %b %d %H:%M:%S %Y")
        print(ccc)
        only_time = strftime("%b:%d:%H:%M:%S", ccc)
        if model_name not in collect.keys(): ## First time in this state
            collect[model_name] = {only_time: {'time': 1, 'users': [user]}}
        else:
            ## in the same state.
            if only_time not in collect[model_name].keys():
                collect[model_name][only_time] = {'time': 1, 'users': [user]}
            else:   
                collect[model_name][only_time]['time'] += 1
                if user not in collect[model_name][only_time]['users']:
                    collect[model_name][only_time]['users'].append(user)


        
        # collect.append(i['_source']['user'])
        # print("---")
    print(collect)
    # print(list(set(collect)))


    ## ------

    # import json
    # from elasticsearch import Elasticsearch

    # hosts = ['10.1.2.102:9200']
    # es = Elasticsearch(hosts=hosts)

    # indices = ['index']

    # # Initialize the scroll
    # page = es.search(
    #     index=','.join(indices),
    #     doc_type='demo',
    #     scroll='2m',
    #     search_type='scan',
    #     size=1000,
    #     q='python'    # 填写 Kibana 搜索栏里的 Lucene 查询语法字符串
    # )
    # sid = page['_scroll_id']
    # scroll_size = page['hits']['total']
    # # print 'total scroll_size: ', scroll_size

    # l = []
    # # Start scrolling
    # while scroll_size > 0:
    #     # print "Scrolling..."
    #     page = es.scroll(scroll_id=sid, scroll='2m')
    #     # Update the scroll ID
    #     sid = page['_scroll_id']
    #     # Get the number of results that we returned in the last scroll
    #     scroll_size = len(page['hits']['hits'])
    #     print("scroll size: " + str(scroll_size))
    #     # Do something with the obtained page
    #     docs = page['hits']['hits']
    #     l += [x['_source'] for x in docs]

    # print 'total docs: ', len(l)

    # file_path = 'demo.json'
    # with open(file_path, 'wb') as f:
    #     json.dump(l, f, indent=2)