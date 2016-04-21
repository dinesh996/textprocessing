import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

df_main= pd.read_json("products_22_03.json")


def specKeys_flattening():
    specKeys = main_df.loc[:,'specKeys']
    #flattening the specKeys values.
    specKeys_flat=[]
    for i in specKeys:
        if isinstance(i,float):
            i=str(i)
            i=''
        for j in i:
            if j!='':
             specKeys_flat.append(j)
    return specKeys_flat
    # specKeys_flat contains the list of all the specKeys.

#Flattening of description.
description= main_df.loc[:,'description']
description_flat=[]
for i in description:
    if i!='':
        description_flat.append(i)
#description_flat contains the flat list of all descriptions.



##To get important parts in a string.
def break_string(a):
    delimiters = [",", ".",";"]
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, a)

def next2(break_string):
    cool={}
    search= ['neck','sleeve','fabric','material','colour','slits']
    for j in break_string:
        for k in search: 
            if k in j:
                wordss= word_tokenize(j)
                x= stopwords.words("english")
                j= [l for l in wordss if l not in x and l!=k]
                cool[k]= " ".join(j)
    return cool




