import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Univariate:
    def __init__(self,df):
        self.df=df
    def colm_details(self,colm):
        print("Details about : "+colm)
        print("Mean "+str(self.df[colm].mean()))
        print("Median " + str(self.df[colm].median()))
        print("Mode " + str(self.df[colm].mode()))

        return

    def create_plot(self,colm):
        #fig = plt.figure()
        #ax = fig.add_subplot(111)

        print('''Is the variable :
              \n1.Categorical 
              \n2.Continuos''')

        colm_type=int(input())

        if colm_type==1:
            print(self.df[colm].value_counts())
            print("\n")
            self.df[colm].value_counts().plot.bar()
            plt.show()
        elif colm_type==2:
            self.colm_details(colm)

            plot_type=int(input("Does Colm contain a ide range of values[0/1]\n"))

            if plot_type==0:
                self.df[colm].value_counts().sort_index().plot.bar()
            else:
                self.df[colm].value_counts().sort_index().plot.line()
            plt.show()
        else:
            return


    def univariate_plot(self):
        print("Enter the column")
        colm=input()

        self.create_plot(colm)