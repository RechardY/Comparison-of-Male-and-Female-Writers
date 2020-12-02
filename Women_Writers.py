import requests
import json

count_1920_female = 0
count_1940_female = 0
count_1960_female = 0
count_1980_female = 0
count_2000_female = 0

url = "http://query.wikidata.org/sparql"

sparql = """

SELECT ?item ?itemLabel ?birth WHERE {
  
  ?item wdt:P27 wd:Q30 .
  ?item wdt:P31 wd:Q5 . 
  ?item wdt:P21 wd:Q6581072 .
  ?item wdt:P569 ?birth .
  ?item wdt:P106 wd:Q36180

  FILTER(
    (year(?birth) >= 1900 && year(?birth) <= 2000)
  )
        
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }

}

"""

params = {
    'query' : sparql
}

headers = {
'Accept' : 'application/json'
}

r = requests.get(url, params=params, headers=headers)

data = json.loads(r.text)

for result in data['results']['bindings']:
  if 'birth' in result:
    if int(result['birth']['value'][0:4]) < 1920:
      count_1920_female = count_1920_female+1
    if int(result['birth']['value'][0:4]) >= 1920 and int(result['birth']['value'][0:4]) < 1940:
      count_1940_female = count_1940_female+1
    if int(result['birth']['value'][0:4]) >= 1940 and int(result['birth']['value'][0:4]) < 1960:
      count_1960_female = count_1960_female+1
    if int(result['birth']['value'][0:4]) >= 1960 and int(result['birth']['value'][0:4]) < 1980:
      count_1980_female = count_1980_female+1
    if int(result['birth']['value'][0:4]) >= 1980:
      count_2000_female = count_2000_female+1

print(count_1920_female)
print(count_1940_female)
print(count_1960_female)
print(count_1980_female)
print(count_2000_female)


