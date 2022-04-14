import json
x =  '{ "name":"dnr", "age":20, "city":"New York"}'
y = json.loads(x)
print(y["age"])
