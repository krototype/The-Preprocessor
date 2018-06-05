'''Data Intake:
Main Script which starts The Preprocessor
Options provided
1.Data Description
2.Data Imputation
3.Univariate Analysis
4.Bivariate Analysis
5.Data Wrangling
6.Download Dataset'''
import pandas as pd
import numpy as np
import sys
import data_impute
import univariate
import bivariate
import download
import wrangling

functionality=[
    "Data_Description",
    "Data_Imputation",
    "Univariate Analysis",
    "Bivariate Analysis",
    "Data Wrangling",
    "Download Dataset"
]
def describe_column(df):
    #Describes a particular column
    print("Enter column name , which you want to describe :")
    colm=input()
    colm=colm.lower()
    print(df[colm].describe())

    input("Press Enter to continue")
    return


def description(df):
    #data description function

    desc_type = 0

    print(df.info())

    while (desc_type != -1):
        print("""Data description :\n 
            1.Numeric Columns Description\n  
            2.Object Column Description\n
            3.Description of a particular Column""")
        desc_type = int(input("Enter -1 to exit this\n"))
        if desc_type == 1:
            print(df.describe(include=[np.number]))
        elif desc_type == 2:
            print(df.describe(include=[np.object]))
        elif desc_type == 3:
            describe_column(df)
        elif desc_type == -1:
            break
        else:
            print("wrong_input")

    return


def find_target(df):
    #function for selecting target variable
    print("List of column names")
    colm_names=list(df.columns.values)

    for colm in colm_names:
        print(colm)

    target=input("Enter the target value ")
    target=target.lower()

    return target


def change_column_lower(df):
    colm_dict={}
    colm_names = list(df.columns.values)
    for colm in colm_names:
        colm_dict[colm]=colm.lower()

    df.rename(columns=colm_dict,inplace=True)

    return df

def preprocessor():
    #Taking dataset as input
    if len(sys.argv)<=1:
        print("\nEnter dataset address")
        df_input=input()
    else:
        df_input=sys.argv[1]

    #Reading the dataset
    df=pd.read_csv(df_input)
    print(" -> Data taken from "+df_input)

    df=change_column_lower(df)

    #deciding the target variable
    target_colm=find_target(df)

    y=df[target_colm]
    x=df.drop(target_colm,axis=1)

    #Menu:
    while(1):
        print("\nWhat do you want")

        count=1
        for i in functionality:
            print(str(count)+". "+i)
            count+=1

        inp=int(input("\nEnter your input: ,-1 to exit\n"))
        if inp==-1:
            exit()
        elif inp==1:
            print(" --> Data Description:")
            description(df)
        elif inp==2:
            print(" --> Data imputation:")
            imp_obj=data_impute.Imputer(df)
            df=imp_obj.impute()
        elif inp==3:
            print(" --> Univariate Analysis:")
            uni_obj=univariate.Univariate(df)
            df=uni_obj.univariate_plot()
        elif inp==4:
            print(" --> Bivariate Analysis:")
            bi_obj = bivariate.Bivariate(df)
            df = bi_obj.bivariate_plot()
        elif inp==6:
            print(" --> Download Dataset")
            down_obj=download.Download(df)
            down_obj.make_dataset()
        elif inp==5:
            print(" --> Data Wrangling")
            wrangle_obj = wrangling.Wrangle(df)
            df=wrangle_obj.wrangle()

    return


if __name__ == "__main__":
    preprocessor()