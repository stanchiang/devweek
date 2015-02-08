import pandas as pd

import pprint
import operator

data=pd.read_csv("testData.csv")


true_data=data[data["is_valid"]==True]


false_data=pd.read_csv('false_negative2.csv')


list_of_false_ip=list(false_data.referer.unique())

results={}
for bad_ip in list_of_false_ip:
	# print bad_ip, data[data['ip']==bad_ip & data['is_valid']==False]/float(len(data[data['ip']==bad_ip] ))
	# aa=len(data[data['ip']==bad_ip & data.is_valid.apply(lambda e: e==False)])


	print bad_ip
	print "===="
	if str(bad_ip)!='nan':

		filter1=data[data['referer']==bad_ip]
		filter2=filter1[filter1['is_valid']==False]
		a1=float(len(filter2))/len(filter1)



	# /float(len(data[data['ip']==bad_ip & data['is_valid']==False]+data[data['ip']==bad_ip & data['is_valid']==True]))

		results.update({bad_ip:a1})


# for site, group in groups:
# 	# print site, list(group['is_valid']).count(False)/float(len(group))
# 	results.update({site:float(list(group['is_valid']).count(False)/float(len(group)))})
# dictionary = sorted(results.items(), key=operator.itemgetter(0))
dictionary= sorted(results.items(), key=lambda x: x[1],reverse=False)
# # print dictionary
final_result={}
for u,v in dictionary:
	print u,":",v
        final_result[u]=v
#pprint.pprint(final_result)

# new_results=pd.DataFrame(results)



