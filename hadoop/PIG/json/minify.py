import json, jsonesque

file = 'tweet.json'
out = 'parsed.json'


with open(file) as json_file:
	s = json_file.read()
	
jsons = []

i = 0
start, end = s.find('{'), s.find('}')
while True:
    try:
        json.loads(s[start:end + 1])
        valid_json = jsonesque.process(s[start:end + 1])
        decoded = json.loads(valid_json)
        jsons.append(decoded)
    except ValueError:
        end = end + 1 + s[end + 1:].find('}')
    else:
        s = s[end + 1:]
        if not s:
            break
        start, end = s.find('{'), s.find('}')
        i+= 1
        if i == 200:
            break

with open(out, 'w') as fp:
    for json_data in jsons:
        json.dump(json_data, fp)
        fp.write("\n")
