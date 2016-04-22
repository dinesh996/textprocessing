import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


main_df= pd.read_json("products_22_04.json")


specKeys = main_df.loc[:,'specKeys']
    #flattening the specKeys values.
specKeys_flat=[]
for i in specKeys:
    if isinstance(i,float):
        i=str(i)
        i=''
    for j in i:
        if j!='':
         specKeys_flat.append(j.lower())
# specKeys_flat contains the list of all the specKeys.

specKeys_list= list(set(specKeys_flat))


tag_value_list=[]
for i in main_df.index:
    if isinstance(main_df.loc[i,'specKeys'],float):
        main_df.loc[i,'specKeys']= str(main_df.loc[i,'specKeys'])
        main_df.loc[i,'specKeys']=''
    if isinstance(main_df.loc[i,'specsValues'],float):
        main_df.loc[i,'specsValues']= str(main_df.loc[i,'specsValues'])
        main_df.loc[i,'specsValues']=''
    for j,k in zip(list(main_df.loc[i,'specKeys']), list(main_df.loc[i,'specsValues'])):
        l1= [j.lower(),k.lower()]
        tag_value_list.append(l1)


key_pool_dict={}
for i in specKeys_list:
    l1=[]
    for j in tag_value_list:
        if i==j[0]:
            l1.append(j[1].lower())
    key_pool_dict[i]= l1

key_pool_unique_dict={}
for j in list(key_pool_dict.keys()):
    key_pool_unique_dict[j]= list(set(key_pool_dict.get(j)))




Main_list=['cloth','price','brand','neck','sleeve','length','behavior','occasion','hide','flaunt','accentuate','draw',
           'design',r'print']


# value_pool=[]
# for i in main_df.index:
#     if isinstance(main_df.loc[i,'specsValues'],float):
#         main_df.loc[i,'specsValues']= str(main_df.loc[i,'specsValues'])
#         main_df.loc[i,'specsValues']=''
#     for k in list(main_df.loc[i,'specsValues']):
#         value_pool.append(k.lower())
# value_pool_set_list= list(set(value_pool)) 



key_aggregator= {}
for j in Main_list:
    l1=[]
    for i in specKeys_list:
        if re.search(j,i):
            l1.append(i)
    key_aggregator[j]= l1


for i in list(key_aggregator.keys()):
    if key_aggregator[i]==[]:
        del key_aggregator[i]


top_tag_value_dict={}
for key in list(key_aggregator.keys()):
    l5=[]
    for j in list(key_aggregator.get(key)):
        if key_pool_unique_dict[j]!='':
            l5.append(key_pool_unique_dict.get(j))
    l5= [m for k in l5 for m in k]
    top_tag_value_dict[key]= l5

value_pool=[i for j in list(top_tag_value_dict.values()) for i in j]


# In given description, finding elements present in our value_pool.


