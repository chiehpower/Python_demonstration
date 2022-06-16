import typesense
import time

def get_time():
    idd = time.time() * 10000000
    idd = '%d' % idd
    idd = int(idd[3:])
    # print(idd)
    return idd

if __name__ == '__main__':

    client = typesense.Client({
    'api_key': 'Hu52dwsas2AdxdE',
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'connection_timeout_seconds': 2
    })

    print(client)
    client.collections['log'].delete()
    try:
        create_response = client.collections.create({
        "name": "log",
        "fields": [
            {"name": "name", "type": "string", "facet": True},
            {"name": "state_id", "type": "int32", "facet": True},
            {"name": "time", "type": "int32"}
        ],
        "default_sorting_field": "time"
        })
    except:
        pass

    # for i in range(50):
    #     record_time = get_time()
    #     print("Record time: ", record_time)
    #     document = {
    #     "name": "chieh",
    #     "state_id": 5215,
    #     "time": record_time
    #     }

    #     client.collections['log'].documents.create(document)

    print("Search the doucment.")

    search_parameters = {
    'q'         : 'chieh',
    'query_by'  : 'name',
    'filter_by' : 'time:>11819174',
    'sort_by'   : 'time:desc',
    'per_page' : 20
    }

    res = client.collections['log'].documents.search(search_parameters)
    print(len(res['hits']))
    for i in range(len(res['hits'])):
        
        print(i, res['hits'][i]['document'])
        print("---")
