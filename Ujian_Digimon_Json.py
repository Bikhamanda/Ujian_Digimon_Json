from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import json

data = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(data.content,'html.parser')
data = soup.find('table', id='digiList')
kolom = []

for i in soup.find_all('th'):
    kolom.append(i.string)

digimon=[]
data=data.find_all('tr')

for item in data[1:]:
    no = item.td.string
    digimon = item.a.string
    image = item.img['src']
    stage = item.center.string
    typeDigimon = item.td.find_next_sibling().find_next_sibling().find_next_sibling()
    attribute = item.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    memory = attribute.find_next_sibling()
    equip_slots = memory.find_next_sibling()
    hp = equip_slots.find_next_sibling()
    sp = hp.find_next_sibling()
    atk = sp.find_next_sibling()
    defense = atk.find_next_sibling()
    intell = defense.find_next_sibling()
    spd = intell.find_next_sibling()
    x = {
        'no' : int(no),
        'digimon' : digimon,
        'image' : image,
        'stage' : stage,
        'type' : typeDigimon.string,
        'attribute' : attribute.string,
        'memory' : memory.string,
        'equip slots' : equip_slots.string,
        'hp' : hp.string,
        'sp' : sp.string,
        'atk' : atk.string,
        'def' : defense.string,
        'int' : intell.string,
        'spd': spd.string}
    digimon.append(x)
# print(digimon)


# # ======= Saving to Json

with open('digimon.json','w') as x:
    x.write(str(digimon).replace("'",'"'))