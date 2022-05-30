### Send the data to the ELK server
from elasticsearch import Elasticsearch
import time
# from elasticsearch_dsl import Search

def check_results(user, index, time_):
    star = time.time()
    # s = Search(using=es, index=index) \
    #     .query("match", user=user) \
    #     .sort({"time": {"order": "desc"}})[:10000]    
    # .filter("range", date={"gte": "now-10d/d","lt": "now/d"}) \
    # response = s.execute()

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
        collect.append(i['_source']['inference_result'])
    # print(collect)
    results = False
    if len(collect) >= time_:
        new_collect = list(set(collect))
        if len(new_collect) == 1 and new_collect[0] == True:
            # print("Results", new_collect)
            results = True
    
    print("Spend: ", time.time()- star)
    return results

def get_time():
    idd = time.time() * 10000000
    idd = '%d' % idd
    idd = int(idd[9:])
    # print(idd)
    return idd

if __name__ == '__main__':
    hosts = ['10.1.2.102:9200']
    es = Elasticsearch(hosts=hosts)
    time_ = 5
    index = 'news'
    user = 'admin'

    ### Delete the index
    print("Delete the index first.")
    res = es.indices.delete(index=index, ignore=[400, 404])
    # print(res)

    ### Create a new index ...
    print("Create a new index ...")
    # result = es.indices.create(index=index, ignore=[400, 404])
    # print(result)

    # inf_f = [False for i in range(10)]
    # inf_t = [True for i in range(40)]
    # inf_f = inf_f + inf_t

    inf_f = [False for i in range(4)]
    inf_t = [True for i in range(5)]
    inf_f1 = [False for i in range(41)]
    inf_f = inf_f + inf_t + inf_f1

    # inf_f = [False for i in range(50)]
    # inf_f = [True]

    print("Start to do inference ...")
    for i in range(20):
        ttt =  get_time() 
        print(f'id={ttt}, and inference_result={inf_f[i]}')
        if inf_f[i]:
            print("********** Ture Case ...")
        data = {'user': 'admin', 'inference_result': inf_f[i], 'time': ttt}
        result = es.create(index=index, doc_type='inference', id=ttt, body=data)
        check = check_results(user, index, time_)
        print(f'check={check}')
        if check:
            print("Success...")
            break

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

