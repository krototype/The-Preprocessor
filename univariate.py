import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Univariate:
    def __init__(self,df):
        self.df=df


    def colm_details(self,colm):
        print(self.df[colm].describe())
        print("\n")
        print("Null count : " + str(self.df[colm].isnull().sum()))
        print("\n")

        return


    def create_plot(self,colm):
        #fig = plt.figure()
        #ax = fig.add_subplot(111)

        print('''Is the variable :
              \n1.Categorical 
              \n2.Continuos''')

        colm_type=int(input())

        if colm_type==1:
            self.colm_details(colm)
            print(self.df[colm].value_counts())
            print("\n")

            print(self.df[colm].value_counts()/len(self.df[colm]))
            print("\n")

            self.df[colm].value_counts().plot.bar()
            plt.show()

        elif colm_type==2:
            self.colm_details(colm)

            print("Do you want histogram[0/1]")
            hist=int(input())
            if hist==1:
                self.df[colm].plot.hist()
                plt.ylabel(colm)
                plt.show()

            print("Do you want lineplot[0/1]")
            linep = int(input())
            if linep == 1:
                self.df[colm].value_counts().sort_index().plot.line()
                plt.ylabel(colm)
                plt.show()

            print("Do you want boxplot[0/1]")
            boxp = int(input())
            if boxp == 1:
                self.df[colm].plot.box()
                plt.ylabel(colm)
                plt.show()

        else:
            return


    def univariate_plot(self):
        print("Enter the column")
        colm=input()

        self.create_plot(colm)