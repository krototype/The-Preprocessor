import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

class Bivariate:

    def __init__(self,df):
        self.df=df


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
        print(self.df.groupby(colm2)[colm1].mean())

        self.df.groupby(colm2)[colm1].mean().plot.bar()
        plt.ylabel(colm1)
        plt.xlabel(colm2)
        plt.show()

        input("Press ENTER to continue")
        return

    def categorical_categorical(self,colm1,colm2):
        print(pd.crosstab(self.df[colm1],self.df[colm2]))

        print(chi2_contingency(pd.crosstab(self.df[colm1],self.df[colm2])))

        self.df.groupby(colm2)[colm1].value_counts().plot.bar()
        plt.ylabel(colm1)
        plt.xlabel(colm2)
        plt.show()

        input("Press ENTER to continue")
        return

    def bivariate_plot(self):
        print("Enter colm 1 :")
        colm1=input()
        type_colm1 = int(input("Is it categorical[0/1] "))

        print("Enter colm 2 :")
        colm2 = input()
        type_colm2 = int(input("Is it categorical[0/1] "))

        if type_colm1==1 and type_colm2==0:
            self.continuous_categorical(colm2 , colm1)
        elif type_colm1==0 and type_colm2==1:
            self.continuous_categorical(colm1 , colm2)
        elif type_colm1==0 and type_colm2==0:
            self.continuous_continuous(colm1 , colm2)
        elif type_colm1==1 and type_colm2==1:
            self.categorical_categorical(colm1 , colm2)

