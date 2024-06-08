from Bio import pairwise2
import math
import statsmodels.api as sm
import numpy as np

def sqrt(x):
    return math.sqrt(x)

def ccf(a,b):
    return(sm.tsa.stattools.ccf(a,b))

def pair(a,b):
    align =  pairwise2.align.globalms(a, b,5, -4, -5, -.1,one_alignment_only = True)
    return (align[-1][0],align[-1][1])

def get_align(l1,l2):
    (l1,l2) = pair(l1,l2)
    mismatch_align =  [ ccf(np.array(quaternion_dict[l1[0]]),np.array(quaternion_dict[l2[0]])) ]
    for i in range(1,len(l1)):
        mismatch_align.append(ccf(np.array(quaternion_dict[l1[i]]),np.array(quaternion_dict[l2[i]])))
    return mismatch_align

quaternion_dict = {}
quaternion_dict['A'] = [0,0,0,1]
quaternion_dict['T'] = [0,2*sqrt(2)/3,0,-1/3]
quaternion_dict['C'] = [0,-sqrt(2)/3,sqrt(6)/3,-1/3]
quaternion_dict['G'] = [0,-sqrt(2)/3,-sqrt(6)/3,-1/3]
quaternion_dict['-'] = [1,0,0,0]

