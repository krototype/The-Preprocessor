'''Bivariate Analysis:
Helps in bivariate analysis of data
Plotting of the data'''

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import seaborn as sns

class Bivariate:

    def __init__(self,df):
        self.df=df

    def correlation_matrix(self):
        print("Do you want correlation matrix[0/1]")
        inp=input()

        if inp=="0":
            return

        corr = self.df.corr()
        sns.heatmap(corr,
                    xticklabels=corr.columns.values,
                    yticklabels=corr.columns.values)
        plt.show()


    def continuous_continuous(self,colm1,colm2):
        self.df.plot.scatter(colm1,colm2)
        plt.xlabel(colm1)
        plt.ylabel(colm2)
        plt.show()

        print("Correlation between {} and {} is ".format(colm1,colm2))
        print(self.df[colm1].corr(self.df[colm2]))

        print('''if between -0.1 to 0.1 - WEAK RELATIONSHIP
                \nif beyond -0.5 to 0.5 - STRONG LINEAR RELATIONSHIP\n''')

        input("Press ENTER to continue")
        return


    def continuous_categorical(self,colm1,colm2):
        print("Mean when grouping according to {}".format(colm2))
        print(self.df.groupby(colm2)[colm1].mean())

        self.df.groupby(colm2)[colm1].mean().plot.bar()
        plt.ylabel(colm1)
        plt.xlabel(colm2)
        plt.show()

        input("Press ENTER to continue")
        return

    def categorical_categorical(self,colm1,colm2):
        stacked_plot=pd.crosstab(self.df[colm1], self.df[colm2])
        print("Cross table of {} and {}".format(colm1,colm2))
        print(pd.crosstab(self.df[colm1],self.df[colm2]))

        print("Chi 2 test :")
        print(chi2_contingency(pd.crosstab(self.df[colm1],self.df[colm2])))


        stacked_plot.plot.bar()
        plt.ylabel(colm1)
        plt.xlabel(colm2)
        plt.show()

        input("Press ENTER to continue")
        return

    def bivariate_plot(self):
        #Landing function
        next_iter="0"

        self.correlation_matrix()

        while(next_iter!="-1"):
            print("Enter colm 1 :")
            colm1=input()
            type_colm1 = int(input("Is it categorical[0/1] "))

            print("Enter colm 2 :")
            colm2 = input()
            type_colm2 = int(input("Is it categorical[0/1] "))

            if type_colm1==1 and type_colm2==0:
                try:
                    self.continuous_categorical(colm2 , colm1)
                except RuntimeError:
                    self.continuous_categorical(colm1, colm2)

            elif type_colm1==0 and type_colm2==1:
                try:
                    self.continuous_categorical(colm1 , colm2)
                except RuntimeError:
                    self.continuous_categorical(colm2, colm1)

            elif type_colm1==0 and type_colm2==0:
                self.continuous_continuous(colm1 , colm2)

            elif type_colm1==1 and type_colm2==1:
                try:
                    self.categorical_categorical(colm1 , colm2)
                except RuntimeError:
                    self.categorical_categorical(colm2, colm1)

            next_iter=input("Press -1 to exit/ Press any other character to continue")


        return self.df

