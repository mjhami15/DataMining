import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from math import *
from decimal import Decimal
from scipy.stats import chi2_contingency

def p_root(value, root):
     
    root_value = 1 / float(root)
    return round (Decimal(value) **
             Decimal(root_value), 3)
 
def minkowski_distance(x, y, p_value):
     
    # pass the p_root function to calculate
    # all the value of vector parallelly
    return (p_root(sum(pow(abs(a-b), p_value)
            for a, b in zip(x, y)), p_value))


lines = []
with open("data.libraries.inventories.txt") as f:
    lines = f.readlines()

cml_raw = lines[1].split("\t")
cbl_raw = lines[2].split("\t")
i = 1
cml = []
cbl = []
while i < 101:
    cml.append(int(cml_raw[i]))
    cbl.append(int(cbl_raw[i]))
    i+=1

cml_prob=[]
for item in cml:
    cml_prob.append(item/sum(cml))

cbl_prob=[]
for item in cbl:
    cbl_prob.append(item/sum(cbl))

j = 0
sum = 0
while j < 100:
    sum += (cml_prob[j]*log(cml_prob[j]/cbl_prob[j]))
    j+=1

a = ((150 - (190*160/3500))**2)/(190*160/3500)
b = ((40 - (190*3340/3500))**2)/(190*3340/3500)
c = ((10 - (160*3310/3500))**2)/(160*3310/3500)
d = ((3300 - (3310*3340/3500))**2)/(3310*3340/3500)

print(a+b+c+d)


obs = np.array([[150, 40],[10,3300]])
print(chi2_contingency(obs))