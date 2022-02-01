from bs4 import BeautifulSoup
import requests
import re


data = requests.get("https://en.wikipedia.org/wiki/List_of_animal_names").text
soup = BeautifulSoup(data,"lxml")
table = soup.select("table",{"class":"wikitable sortable jquery-tablesorter"})[2]
clean_data = lambda x: re.sub("\[[0-9]+\]", '', x.strip().replace('\xa0', '').replace(':', ''))
headers = [header.text for header in table.find_all('th')]
results = [{headers[i]: clean_data(cell.text) for i, cell in enumerate(row.find_all('td'))}
           for row in table.find_all('tr')]

data={}
for dict in results:
    if dict == {}:
        continue
    data[dict['Animal']] = {i:dict[i] for i in headers[1:6]}

spliter= lambda x: clean_data(x).split() if (' ' in x) else clean_data(x)

all_Collateral_adjective = []

for keys,values in data.items():
    values['Collateral adjective'] = spliter(values['Collateral adjective'])
    a = values['Collateral adjective']

    if type(a) == list:
        for adj in a:
            all_Collateral_adjective.append(adj)

    else:
        all_Collateral_adjective.append(a)



all_Collateral_adjective = set(all_Collateral_adjective)
all_Collateral_adjective_dict = {k: [] for k in all_Collateral_adjective}
for key,value in data.items():
    b = value['Collateral adjective']
    if type(b) == list:
        for g in b:
            all_Collateral_adjective_dict[g].append(key)
    else:
        all_Collateral_adjective_dict[b].append(key)


print(all_Collateral_adjective_dict)