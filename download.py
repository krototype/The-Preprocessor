'''Download
Helps in downloading the dataset after wrangling it up'''

import pandas as pd
import numpy as np

class Download:
    def __init__(self,df):
        self.df=df


    def make_dataset(self):
        final_df = {}
        colm_names = list(self.df.columns.values)
        count=0
        for colm in colm_names:
            final_df[count]=self.df[colm]
            count+=1

        dataset = pd.DataFrame(final_df)
        name=input("Enter the name with which you want to save the dataset ")
        name=name+".csv"
        dataset.to_csv(name,index=False, header=colm_names)

        print("Done!!!")

        return