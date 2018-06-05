'''Wrangle:
Helps in wrangling the data ,options provided:
1.One Hot Encoding
2.Normalization
3.Dropping of columns'''

import pandas as pd
import numpy as np
from sklearn import preprocessing

functionality=['One Hot Encode',
               'Normalization',
               'Dropping Column']

class Wrangle:
    def __init__(self, df):
        self.df=df


    def onehot(self):
        print("Enter the columns which you want to one hot encode (Make sure that colm can be encoded)")
        num_colm=int(input("Enter the number of columns you want to encode "))
        colm_list=[]
        for i in range(num_colm):
            colm=input("Enter the column name: ")
            colm = colm.lower()
            colm_list.append(colm)

        self.df=pd.get_dummies(data=self.df , columns=colm_list)

        input("Done :O !!\nPress enter to continue")
        return self.df

    def normalize(self):
        while(1):
            print('''1. Normalizing whole dataset(Everything shall be numeric)
                  \n2. Normalize a column''')

            type=input("-1 to exit ")

            if type=="1":
                print("Normalizing whole dataset (Everything shall be numeric)")
                min_max_scaler = preprocessing.MinMaxScaler()

                # Create an object to transform the data to fit minmax processor
                scaled = min_max_scaler.fit_transform(self.df)

                # Run the normalizer on the dataframe
                self.df = pd.DataFrame(scaled)

            elif type=="2":
                print("Normalizing a column")
                colm=input("Enter the colm ")
                colm=colm.lower()
                self.df[colm]=(self.df[colm]-self.df[colm].min())/(self.df[colm].max()-self.df[colm].min())

            elif type=="-1":
                return self.df

            input("Done :P !! Press Enter to continue")


    def column_drop(self):

        while(1):
            print("Enter the column you want to drop")
            colm=input("Enter -1 to exit\n")
            colm=colm.lower()

            if colm=="-1":
                break

            self.df=self.df.drop(colm,axis=1)
            input("Dropped :D !!\nPress enter to continue")
        return self.df


    def wrangle(self):

        while(1):
            print("Features provided:\n")

            count=1
            for i in functionality:
                print(str(count)+". "+i)
                count+=1

            select_option=input("Enter -1 to exit")

            if select_option=="1":
                self.df=self.onehot()

            elif select_option=="2":
                self.df=self.normalize()

            elif select_option=="3":
                self.df=self.column_drop()

            elif select_option=="-1":
                return self.df

