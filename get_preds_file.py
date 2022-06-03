import numpy as np
import os
import json

sort_ids = np.load('sort_ids.npy')
n = sort_ids.shape[0]

dataset_path = 'C:/Users/Krishnam/Desktop/TCS_intern/NeuralCodeSum/preprocess_data/check_test.jsonl'
indexs = []
with open(dataset_path) as f:
    for line in f:
        line = line.strip()
        js = json.loads(line)
        indexs.append(int(js['index']))

final_path = 'C:/Users/Krishnam/Desktop/TCS_intern/NeuralCodeSum/final_scores/predictions.jsonl'
with open(final_path,'w') as f:
    for index,sort_id in zip(indexs,sort_ids):
        js={}
        js['index']=int(index)
        js['answers']=[]
        # for idx in sort_id[:499]:
        for idx in sort_id[:99]:
            js['answers'].append(indexs[int(idx)])
        f.write(json.dumps(js)+'\n')


