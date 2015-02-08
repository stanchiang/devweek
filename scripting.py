import pandas as pd

import pprint

data=pd.read_csv("testData.csv")


true_data=data[data["is_valid"]==True]


false_data=data[data["is_valid"]==False]




groups=data.groupby("referer")
results={}
for site, group in groups:
	print site, list(group['is_valid']).count(False)/float(len(group))
	results.update({site:float(list(group['is_valid']).count(False)/float(len(group)))})

dictionary= sorted(results.items(), key=lambda x: x[1],reverse=False)
print dictionary
final_result={}
for u,v in dictionary:
	print u,":",v
        final_result[u]=v
#pprint.pprint(final_result)



