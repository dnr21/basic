import json
a = '{"name": "rocky", "language": "English"}'
y = json.loads(a)
print("JSON string = ", y)
print()
f = open ('data.json', "r")
data = json.loads(f.read())
for i in data['std_details']:
	print(i)
f.close()
