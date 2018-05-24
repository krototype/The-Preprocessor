# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:06:43 2018

@author: hp
"""

import pandas as pd
import numpy as np
import sys
import data_impute
import univariate

functionality=[
    "Data_Description",
    "Data_Imputation",
    "Univariate Analysis"
]

def description(df):
    desc_type = 0

    print(df.info())

    while (desc_type != -1):
        print("""Data description :\n 
            1.Numeric Columns Description\n  
            2.Object Column Description\n""")
        desc_type = int(input("Enter -1 to exit this\n"))
        if desc_type == 1:
            print(df.describe(include=[np.number]))
        elif desc_type == 2:
            print(df.describe(include=[np.object]))
        elif desc_type == -1:
            break
        else:
            print("wrong_input")

    return

def find_target(df):
    print("List of column names")
    colm_names=list(df.columns.values)

    for colm in colm_names:
        print(colm)

    target=input("Enter the target value")

    return target


if len(sys.argv)<=1:
    print("\nEnter dataset address")
    df_input=input()
else:
    df_input=sys.argv[1]
    

df=pd.read_csv(df_input)
print(" -> Data taken from "+df_input)

target_colm=find_target(df)

y=df[target_colm]
X=df.drop(target_colm,axis=1)

while(1):
    print("\nWhat do you want")

    c=1
    for i in functionality:
        print(str(c)+". "+i)
        c+=1

    inp=int(input("\nEnter your input: ,-1 to exit\n"))
    if inp==-1:
        exit()
    elif inp==1:
        print(" --> Data Description:")
        description(X)
    elif inp==2:
        print(" --> Data imputation:")
        imp_obj=data_impute.Imputer(X)
        df=imp_obj.impute()
    elif inp==3:
        print(" --> Univariate Analysis:")
        uni_obj=univariate.Univariate(X)
        df=uni_obj.univariate_plot()

