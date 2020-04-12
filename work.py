from sklearn import datasets
import pandas as pd
import numpy as np

context="""This dataset contains complete information about 
various aspects of crimes happened in India from 2001.
There are many factors that can be analysed from this dataset. Over all, 
I hope this dataset helps us to understand better about India."""

insp='''
There could be many things one can understand by analyzing this dataset. Few inspirations for you to start with.
1.What is the major reason people being kidnapped in each and every state?
2.Offenders relation to the rape victim
3.Juveniles family background, education and economic setup.
4.Which state has more crime against children and women?
5.Age group wise murder victim
6.Crime by place of occurrence.
7.Anti corruption cases vs arrests.
8.Which state has more number of complaints against police?
9.Which state is the safest for foreigners?'''

#loading data from our csv file
data_rape=pd.read_csv('data\Victims_of_rape.csv',delimiter=',')

#defining the functions to get the data from our files
def get_col_rape():
    return data_rape.columns

def get_dataR_head():
    return data_rape

