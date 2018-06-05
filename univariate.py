'''Univariate Analysis:
Helps in analysis of continuous/categorical data

1. Data description
2.Plotting of data '''

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np
import pandas as pd


class Univariate:
    
    def __init__(self,df):
        self.df=df


    def colm_details(self,colm):
        #Describes the details for the columns
        print(self.df[colm].describe())
        print("\n")
        print("Null count : " + str(self.df[colm].isnull().sum()))

        return


    def create_plot(self,colm):
        #Creates the plot for the function
        print('''Is the variable :
              \n1.Categorical 
              \n2.Continuos''')

        colm_type=int(input())

        if colm_type==1:
            #Categorical Data Analysis
            print("Column Details:")
            self.colm_details(colm)
            print("Individual category total count:")
            print(self.df[colm].value_counts())
            print("\n")

            print("Individual category percentage count:")
            print(self.df[colm].value_counts()/len(self.df[colm]))
            print("\n")

            self.df[colm].value_counts().plot.bar()
            plt.show()

        elif colm_type==2:
            #Continuous Data Analysis
            print("Column Details:")
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

        input("Press ENTER to continue")
        return


    def univariate_plot(self):
        #landing function from data_intake

        while(1):
            print("Enter the column , which you want to analyse")
            colm=input("Enter -1 to exit ")
            colm = colm.lower()

            if colm=="-1":
                break;

            #calling the function to create the plot and describe the column
            self.create_plot(colm)

        return self.df