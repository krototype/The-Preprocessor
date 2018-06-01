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

import pandas as pd
import numpy as np

class Imputer:

    def __init__(self,df):
        self.df=df


    def colm_rem(self,colm):
        #Removes the column from the dataset
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
        #Fills the column with given value
        print("You can fill the column with element of your choice")

        if colm_type=="obj":
            fill_with = input("Enter the value to fill with")
        else:
            fill_with = int(input("Enter the value to fill with"))

        self.df[colm] = self.df[colm].fillna(fill_with)

        return


    def colm_avg(self,colm):
        #fills the column with avg data
        print("Filling the nan values with the average of the column")

        self.df[colm] = self.df[colm].fillna(self.df[colm].mean())

        return


    def colm_median(self,colm):
        #fills the column with median of data
        print("Filling the nan values with the average of the column")

        self.df[colm] = self.df[colm].fillna(self.df[colm].median())

        return


    def colm_mode(self,colm):
        #fills the column with mode of data
        print("Filling the nan values with the average of the column")

        self.df[colm] = self.df[colm].fillna(self.df[colm].mode()[0])

        return

    def suggest_imp(self,colm_names):
        #loops through all the column and asks for imputation if needed
        for colm in colm_names:
            colm_null=sum(pd.isnull(self.df[colm]))

            if colm_null==0:
                print("Column Name - "+colm + " has no null values")

            else:
                if self.df[colm].dtype=="object":
                    print(colm + " is of object type\n")
                    print(colm_null)
                    print('''1. Column Removal 
                            \n2. Fill with some value
                            \n3. Fill Mode value
                            \n4.Ignore\n''')

                    removal_inp=int(input())

                    if removal_inp==1:
                        self.colm_rem(colm)
                    elif removal_inp==2:
                        self.colm_fill(colm,"obj")
                    elif removal_inp==3:
                        self.colm_mode(colm)
                    else:
                        print("Ignoring "+colm+" imputation")

                else:
                    print(colm + " is of numeric type\n")
                    print(colm_null)
                    print('''1. Column Removal 
                            \n2. Fill with some value 
                            \n3. Fill Average value
                            \n4. Fill Median value
                            \n5. Fill Mode value
                            \n6.Ignore\n''')

                    removal_inp = int(input())

                    if removal_inp==1:
                        self.colm_rem(colm)
                    elif removal_inp==2:
                        self.colm_fill(colm,"num")
                    elif removal_inp==3:
                        self.colm_avg(colm)
                    elif removal_inp==4:
                        self.colm_median(colm)
                    elif removal_inp==5:
                        self.colm_mode(colm)
                    else:
                        print("Ignoring "+colm+" imputation")
                        continue

            input("Press enter to move to next column")

        return

    def impute(self):
        #Landing function from data_intake
        colm_names=list(self.df.columns.values)

        #Printing null count of the columns
        print("column - "+"Null Count")
        for colm in colm_names:
            print(str(colm)+" - "+str(sum(pd.isnull(self.df[colm]))))

        procede_inp=input("Enter -1 to return , press any key to impute")
        if procede_inp=="-1":
            return
        self.suggest_imp(colm_names)
        return self.df