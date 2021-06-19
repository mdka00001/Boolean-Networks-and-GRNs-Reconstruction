from code import Noise
import pandas as pd
import csv
import operator
import math
import numpy as np
from scipy import stats
import sys

class Refine:
    def __init__(self, path):
        with open(path, 'r') as handle:
            table=csv.reader(handle, delimiter="\t")
            df=pd.DataFrame(table)
            new_header = df.iloc[0]
            df_head = df[1:]
            df_head.columns = new_header
            df_head1=df_head.drop("strain", axis=1)
            df_head1=df_head1.astype(float)

            ttst1=pd.DataFrame()
            ttst2=[]
                   
                   

            for i in df_head1:
                ttst3=[]
                p=stats.ttest_ind(df_head1[i], df_head1)
                ttst3.append(p[1])
                ttst4=pd.DataFrame(ttst3)
            
                ttst1=pd.concat([ttst1, ttst4], axis=0)

            ttst1.columns=new_header[1:]
            ttst1.reset_index(inplace=True)
            final_df_4=ttst1.drop(columns="index")

            row_names=["G1(-/-)","G2(-/-)","G3(-/-)","G4(-/-)","G5(-/-)","G6(-/-)","G7(-/-)","G8(-/-)","G9(-/-)","G10(-/-)",]
            row=pd.DataFrame(row_names)

            ttst_final=pd.concat([row, final_df_4], axis=1)
            ttst_final.columns=new_header
            ttst_final2=ttst_final.set_index("strain")

            stdoutOrigin=sys.stdout 
            sys.stdout = open("refined.txt", "w")
            for i in ttst_final2.columns:
                k=ttst_final2[i]<0.05
                l=ttst_final2[k]
                print(l)
            stdoutOrigin=sys.stdout 
            sys.stdout = open("refined.txt", "w")
            

            

            