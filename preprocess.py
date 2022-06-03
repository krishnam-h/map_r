# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import os
import json
from tqdm import tqdm
def files(path):
    g = os.walk(path) 
    file=[]
    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            file.append(os.path.join(path, file_name))
    return file

cont=0
with open("train.jsonl",'w') as f:
    for i in tqdm(range(1,65),total=64):
        items=files("../POJ-104/{}".format(i))
        for item in items:
            js={}
            js['label']=item.split('/')[2].split('\\')[0]
            js['index']=str(cont)
            js['code']=open(item,encoding='latin-1').read()
            f.write(json.dumps(js)+'\n')
            cont+=1
test_codes1 = []         
with open("valid.jsonl",'w') as f:
    for i in tqdm(range(65,81),total=16):
        items=files("../POJ-104/{}".format(i))
        for item in items:
            js={}
            js['label']=item.split('/')[2].split('\\')[0]
            js['index']=str(cont)
            js['code']=open(item,encoding='latin-1').read()
            cod = str(js['code']).replace("\n", "")
            test_codes1.append(cod)
            f.write(json.dumps(js)+'\n')
            cont+=1

with open("../data/C/dev/code.original",'w', encoding="utf-8") as f:
    for i in range(len(test_codes1)):                      # here change to test_codes[:1000] for smaller dataset
        f.write(test_codes1[i] + '\n')

test_codes2 = []      
with open("test.jsonl",'w') as f:
    for i in tqdm(range(81,195),total=24):
        items=files("../POJ-104/{}".format(i))
        for item in items:
            js={}
            js['label']=item.split('/')[2].split('\\')[0]
            js['index']=str(cont)
            js['code']=open(item,encoding='latin-1').read()
            cod = str(js['code']).replace("\n", "")
            test_codes2.append(cod)
            f.write(json.dumps(js)+'\n')
            cont+=1
            

with open("../data/C/test/code.original",'w', encoding="utf-8") as f:
    for i in range(len(test_codes2)):                      # here change to test_codes[:1000] for smaller dataset
        f.write(test_codes2[i] + '\n')