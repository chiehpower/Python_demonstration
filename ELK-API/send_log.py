### Send the data to the ELK server
print("Please use Python 3.8.")
import sys
pythonversion = sys.version
print("Your Python version is: ", pythonversion)
if pythonversion[:3] == '3.6':
    raise 'Cannot use Python 3.6'
from elasticsearch import Elasticsearch
import time
from time import ctime

# from elasticsearch_dsl import Search

def check_results(user, index, time_):
    star = time.time()
    # s = Search(using=es, index=index) \
    #     .query("match", user=user) \
    #     .sort({"time": {"order": "desc"}})[:10000]    
    # .filter("range", date={"gte": "now-10d/d","lt": "now/d"}) \
    # response = s.execute()
    print("User: ", user, "index:", index, "time:", time_)
    searchBody = {
        "sort" : [
            {"time" : {"order" : "desc"}}
        ],
        "size": time_,
        "query" : {
            "bool": {
            "must": {
                "match": { 
                    "user": user
                }
            }
            }        
        }
    }
    es.indices.refresh(index)

    response = es.search(
        index=index, body=searchBody)

    # print(response)
    collect = []
    for i in response["hits"]['hits']:
        # print(i)
        # print(i['_source']['inference_result'])
        ConvertbackTime(i['_source']['time'])
        collect.append(i['_source']['time'])
        print("---")
    # print(collect)
    # results = False
    # if len(collect) >= time_:
    #     new_collect = list(set(collect))
    #     if len(new_collect) == 1 and new_collect[0] == True:
    #         # print("Results", new_collect)
    #         results = True
    
    print("Spend: ", time.time()- star)
    return collect

def get_time():
    idd = time.time() * 10000000
    idd = '%d' % idd
    idd = int(idd)
    # print(idd)
    return idd

def ConvertbackTime(number):
    idd = number / 10000000
    print('Today is: ',ctime(idd))
    # print(idd)

if __name__ == '__main__':
    # hosts = ['10.1.2.102:9200'] 
    hosts = ['10.1.2.84:9200']
    es = Elasticsearch(hosts=hosts)
    time_ = 50
    index = 'news'
    user = 'admin'

    ### Delete the index
    print(">>> Delete the index first.")
    # res = es.indices.delete(index=index, ignore=[400, 404])
    # print(res)



    ### Create a new index ...
    print(">>> Create a new index ...")
    checkindex = es.indices.exists(index=index)
    if checkindex:
        print('Already existed')
    else:
        result = es.indices.create(index=index, ignore=[400, 404])
        print(result)

    try:
        body = {"index.blocks.read_only_allow_delete": "false"}
        es_index_settings = es.indices.put_settings(index=index,body=body)
    except elasticsearch.ElasticsearchException as exp:
        print(exp)

    # inf_f = [False for i in range(10)]
    # inf_t = [True for i in range(40)]
    # inf_f = inf_f + inf_t

    # inf_f = [False for i in range(4)]
    # inf_t = [True for i in range(5)]
    # inf_f1 = [False for i in range(41)]
    # inf_f = inf_f + inf_t + inf_f1

    inf_f = [2123 for i in range(4)]
    inf_t = [3400 for i in range(5)]
    inf_f1 = [99999 for i in range(41)]
    inf_f = inf_f + inf_t + inf_f1

    # inf_f = [False for i in range(50)]
    # inf_f = [True]

    print(">>> Start to do inference ...")
    for i in range(20):
        ttt =  get_time() 
        print(f'id= {ttt}, and state= {inf_f[i]}')
        # if inf_f[i]:
            # print("********** Ture Case ...")
        data = {'user': 'admin', 'state_id': inf_f[i], 'time': ttt}
        print(data)
        # result = es.create(index=index, doc_type='inference', id=ttt, body=data)
        result = es.create(index=index, doc_type='inference', id=ttt, document=data)

        check = check_results(user, index, time_)
    print("Results: ")
    print(check)
        # print(f'check={check}')
        # if check:
        #     print("Success...")
        #     break

    ##############
    # ttt =  get_time()
    # data = {'user': '123', 'inference_result': False, 'time':ttt}
    # print(ttt)
    # result = es.create(index='news', doc_type='inference', id= ttt, body=data)

    # # ### Get the data from the ELK server
    # print("----"*5)
    # time.sleep(0.1)
    # result = es.search(index='news', doc_type='inference', size=15)
    # for i in result['hits']['hits']:
    #     print(i)
    #     print("---")
    # print("Total:", len(result['hits']['hits']))

    #### Use elasticsearch_dsl packages.
    # from elasticsearch_dsl import Search
    # s = Search(using=es, index="news") \
    #     .query("match", user="123") \
    #     .sort({"_id": {"order": "desc"}})[:15]    
    #     # .filter("range", date={"gte": "now-10d/d","lt": "now/d"}) \


    # response = s.execute()
    # collect = []
    # for i in response["hits"]["hits"]:
    #     collect.append(i['_source']['inference_result'])


    # new_collect = set(collect)
    # print(collect)
    # print(new_collect)

    # if len(new_collect) != 1:
    #     print("False")
        
    # print(response["hits"]["total"]["value"])  

    # documents = [
    #     {"index":{"_id" : ttt}},
    #     { "stock_id":"0050", "date":"2020-09-11", "volume":2905291,"open":103.20,"high":105.35, "low":103.80, "close":104.25 },
    # ]

    # result = es.bulk(body=documents, index='news', doc_type='test')
    # print(result)

