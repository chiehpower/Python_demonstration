import typesense

client = typesense.Client({
  'api_key': 'Hu52dwsas2AdxdE',
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 2
})

# create_response = client.collections.create({
#   "name": "companies",
#   "fields": [
#     {"name": "company_name", "type": "string" },
#     {"name": "num_employees", "type": "int32" },
#     {"name": "country", "type": "string", "facet": True }
#   ],
#   "default_sorting_field": "num_employees"
# })


# document = {
#  "id": "124",
#  "company_name": "Stark Industries",
#  "num_employees": 5215,
#  "country": "USA"
# }

# client.collections['companies'].documents.create(document)

print("Search the doucment.")
search_parameters = {
  'q'         : 'stork',
  'query_by'  : 'company_name',
  'filter_by' : 'num_employees:>100',
  'sort_by'   : 'num_employees:desc'
}

print(client.collections['companies'].documents.search(search_parameters))
