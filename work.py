from sklearn import datasets
import pandas as pd
import numpy as np

data1 =datasets.load_boston()
def d_keys():
    
    return data1.keys()

def d_columns():
    return data1.feature_names

def d_desc():
    return data1.DESCR

