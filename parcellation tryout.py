import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import datetime
import math
import pandas as pd
import random
random.seed(2)

building = [['n','n','e','e','n','n','n','e','e','n','n','n','e','e','n','n'],
            ['n','n','e','e','n','n','n','e','e','n','n','n','e','e','n','n'],
            ['n','n','e','e','n','n','n','e','e','n','n','n','e','e','n','n']]

def questions(cohabitation,age,ppl,room,study):
    
    
    return number_of_nodes

def parcellation(demands, building):
    return parcellated_building

a = ['n','n','e','e','n','n','n','e','e','n','n','n','e','e','n','n']
k= "".join(a)

##########################################################################

c=0
all_list= []

while c<len(a):
    for j in range(c,len(a)+1):
        #print(c,j)
        s = ""
        s = s.join(a[c:j])
        all_list.append(s)
        #print(s)
    c+=1
valid_list= []

for i in all_list:
    #print(i,len(i),i.find('e'))
    if len(i) >= 2 and i.find('e')>=0:
        valid_list.append(i)

unique_list = np.unique(valid_list).tolist()

unique_list = sorted(unique_list,key=len)


##################################################################

k_list = []
out_list = []
for a in unique_list:
    k_list.append(k)
    out_list.append("")

combi_list = []

def find_permuatations(unique_list,k_list,out_list):
    for i in range(0,len(unique_list)):
        if len(out_list[i].replace('(','').replace(')',''))<16:
            idx = k_list[i].find(unique_list[i])
            if idx >= 0 and len(k_list[i])>0:
                out_list[i] += k_list[i][0:idx] + '(' + unique_list[i]+ ')'
                skip = idx + len(unique_list[i])
                p = out_list[i]+k_list[i][skip::]
                k_list[i] = k_list[i][skip::]
                combi_list.append(p)
                print(p)
                k_list2 = []
                out_list2 = []
                for a in unique_list:
                    k_list2.append(k_list[i])
                    out_list2.append(out_list[i])
                find_permuatations(unique_list,k_list2,out_list2)
            
find_permuatations(unique_list,k_list,out_list)          
        
combi_list_q = np.unique(combi_list).tolist()

valid_combi = []

############################################################

unique_list.remove('ee')
unique_list.remove('een')
unique_list.remove('nee')
unique_list.remove('eennnee')
unique_list.remove('eennneen')
unique_list.remove('neennnee')
unique_list.remove('neennneen')
unique_list.remove('eennneennn')
unique_list.remove('nnneennnee')
unique_list.remove('eennneennne')
unique_list.remove('ennneennnee')
unique_list.remove('neennneennn')
unique_list.remove('nnneennneen')
unique_list.remove('eennneennnee')
unique_list.remove('ennneennneen')
unique_list.remove('neennneennne')
unique_list.remove('eennneennneen')
unique_list.remove('neennneennnee')
unique_list.remove('eennneennneenn')
unique_list.remove('neennneennneen')

import re

a1 = []
for i in unique_list:
    a1.append([m.start() for m in re.finditer(i, k)])
    
    
####################################################################
    
