import json
def sort_by_price_ascending(json_string):
    json_data = json.loads(json_string)
    json_data = sorted(json_data, key= lambda i: (i['price'], i['name']))
    return json.dumps(json_data)

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))