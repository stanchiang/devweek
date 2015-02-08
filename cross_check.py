import pandas as pd

category=True

data=pd.read_csv("false_negative2.csv")

original_data=pd.read_csv("testData.csv")


categories=list(data['user_agent'].unique())
results={}
for category in categories:
	# print category
	filter_data=original_data[original_data['user_agent']==category]
	# print 
	# print float(filter_data['is_valid'].value_counts()[True])/(filter_data['is_valid'].value_counts()[True]+filter_data['is_valid'].value_counts()[False])
	# print '==========='
	results.update({category:float(filter_data['is_valid'].value_counts()[True])/(filter_data['is_valid'].value_counts()[True]+filter_data['is_valid'].value_counts()[False])})



dictionary= sorted(results.items(), key=lambda x: x[1],reverse=False)
# # print dictionary
final_result={}
for u,v in dictionary:
	print u,":",v
        final_result[u]=v
# new_data=data[data['is_valid']==category]


# new_data.to_csv(str(category)+".csv")


# print data['is_valid'].value_counts()


# new_data=data[data.referer.apply(lambda e: str(e).lower()=='nan')]

# print new_data['is_valid'].value_counts()
