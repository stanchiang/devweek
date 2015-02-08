import pandas as pd 
import pprint
from time import sleep
data=pd.read_csv("testData.csv")
true_data=pd.read_csv("True.csv")
false_data=pd.read_csv("false_negative2.csv")





bad_id=dict(false_data['ip'].value_counts())

list_bad_id=list(bad_id.keys())


# for key in list_bad_id:
	# print key, len(true_data[true_data['ip']==key])




# print "=========="
# pprint.pprint(bad_id)




import pandas as pd

import pprint
import operator

data=pd.read_csv("testData.csv")


true_data=data[data["is_valid"]==True]


false_data=data[data["is_valid"]==False]




groups=data.groupby("user_agent")



bad_user_agents=list(false_data['user_agent'].unique())















bad_referers=list(false_data['referer'].unique())



results={}
for bad_id in list_bad_id:

	for user_agent in bad_user_agents:
		# print bad_id, "======", user_agent

		for referer in bad_referers:
			filter_data=data[data.user_agent.apply(lambda e: str(e)==user_agent) & data.ip.apply(lambda e: str(e) ==bad_id) & data.referer.apply(lambda e: str(e) ==referer)]
			if len(filter_data)>0:
				if sum(list(filter_data['is_valid']))>0:
					real_filter=filter_data
					print real_filter
					# sleep()

			# AA=real_filter['is_valid'].count(False)   


			# results.update({str(bad_id)+'|'+str(user_agent):AA})


# dictionary= sorted(results.items(), key=lambda x: x[1],reverse=False)
# # # print dictionary
# final_result={}
# for u,v in dictionary:
# 	print u,":",v
#         final_result[u]=v

# # pprint.pprint(final_result)








