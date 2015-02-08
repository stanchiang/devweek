black_list=['127.0.0.01','127.0.0.1','193.', '192.168.','.10.10.10','.20.10.10',




'172.16',
'172.17',
'172.18',
'172.19',
'172.20',
'172.21',
'172.22',
'172.23',
'172.24',
'172.25',
'172.26',
'172.27',
'172.28',
'172.29',
'172.30',
'172.31',
'172.32',
'66.249.64.120',
'180.76.5.148',


 ]



black_list_url=[
'http://onetwotrip.com',
'http://shmoogle.com',
'http://localhost',
'http://127.0.0.1',
'http://aviasales.ru',
'http://faceboook.com', 
'http://darknet.info',




 ]


def boot_rule(ip,user_agent,referer):
    ip=str(ip)
    user_agent=str(user_agent)
    referer=str(referer)
    #rule 1 invalid loopback address
    # risk1=0
    if any(item in ip for item in black_list ):
        return 1


    if ip[:2]=="10.":
        return 1


    #rule 2: no user_agent:
    if str(user_agent).lower()=='nan' or user_agent==None or user_agent=='':
        return 1


    if any(item==referer for item in black_list_url):
        return 1


    if len(user_agent)<15 and 'w3m' not in user_agent:
        return 1

    return 0





if __name__ == '__main__':
    #load data
    import pandas as pd
    data=pd.read_csv("testData.csv")
    false_list=[]
    true_list=[]
    false_positive_list=[]

    df = pd.DataFrame(columns=('ip', 'user_agent', 'referer'))

    # f=open("new_false_negative.txt","w")
    # text=''
    j=1

    for i in range(len(data)):
        if boot_rule(data['ip'].irow(i),data['user_agent'].irow(i),data['referer'].irow(i))==0:
            false_list.append(i)
            if data['is_valid'].irow(i)==True:
                false_positive_list.append[i]
        # else:
        #     true_list.append[i]
        #     if data['is_valid'].irow(i)==Fa






            
   
            df.loc[j,'ip'] =str(data['ip'].irow(i))
            df.loc[j,'user_agent']=str(data['user_agent'].irow(i))
            df.loc[j,'referer']=str(data['referer'].irow(i))

            j+=1
    df.to_csv("false_negative3.csv",sep='\t')


    print "number of false: ", len(false_list)

    print "recall rate: ", len(false_list)/float(len(data))


    print "false positive", len(false_positive_list)/float(len(false_list))









    # print 'false positive: '
















