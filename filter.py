import pandas as pd

category=True

data=pd.read_csv("testData.csv")


# new_data=data[data['is_valid']==category]


# new_data.to_csv(str(category)+".csv")


# print data['is_valid'].value_counts()


new_data=data[data.referer.apply(lambda e: str(e).lower()=='nan')]

print new_data['is_valid'].value_counts()
