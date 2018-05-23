# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:25:12 2018

@author: hp
"""
'''
Imputation:
Helps in filling up the null values

Method1:
Removal of null rows

Method2:
Filling null values with specified values

Method3:
Filling null values with average values
'''
#import data_intake
import pandas as pd
import numpy as np

class Imputer:
    def __init__(self,df):
        self.df=df

    def colm_rem(self,colm):
        print("Removing the null value rows of "+colm)
        temp_df=self.df[pd.notnull(self.df[colm])]
        print(temp_df.describe())

        print("\n Do you want to keep the changes[0/1]\n")

        colm_rem_inp=int(input())

        if colm_rem_inp==1:
            print("updating column")
            self.df=temp_df

        return

    def colm_fill(self,colm,colm_type):
        print("You can fill the column with element of your choice")

        if colm_type=="obj":
            fill_with = input("Enter the value to fill with")
        else:
            fill_with = int(input("Enter the value to fill with"))

        self.df[colm] = self.df[colm].fillna(fill_with)

        return

    def colm_avg(self,colm):
        print("Filling the nan values with the average of the column")

        self.df[colm] = self.df[colm].fillna(self.df[colm].mean())

        return

    def suggest_imp(self,colm_names):
        for colm in colm_names:
            colm_null=sum(pd.isnull(self.df[colm]))

            if colm_null==0:
                print("Column Name - "+colm + " has no null values")
                continue
            else:
                if self.df[colm].dtype=="object":
                    print(colm + " is of object type\n")
                    print(colm_null)
                    print('''1. Column Removal 
                            \n2. Fill with some value
                            \n3.Ignore\n''')

                    removal_inp=int(input())

                    if removal_inp==1:
                        self.colm_rem(colm)
                    elif removal_inp==2:
                        self.colm_fill(colm,"obj")
                    else:
                        print("Ignoring "+colm+" imputation")
                        continue

                else:
                    print(colm + " is of numeric type\n")
                    print(colm_null)
                    print('''1. Column Removal 
                            \n2. Fill with some value 
                            \n3. Fill Average value
                            \n4.Ignore\n''')

                    removal_inp = int(input())

                    if removal_inp==1:
                        self.colm_rem(colm)
                    elif removal_inp==2:
                        self.colm_fill(colm,"num")
                    elif removal_inp==3:
                        self.colm_avg(colm)
                    else:
                        print("Ignoring "+colm+" imputation")
                        continue

        return

    def impute(self):
        colm_names=list(self.df.columns.values)
        print("column - "+"Null Count")
        for colm in colm_names:
            print(str(colm)+" - "+str(sum(pd.isnull(self.df[colm]))))

        procede_inp=int(input("Enter -1 to return , press any key to impute"))
        if procede_inp==-1:
            return
        self.suggest_imp(colm_names)
        return self.df