import pandas as pd
import csv
import operator
import math
import numpy as np
from scipy import stats
import sys

class Noise:
    def __init__(self, path):
        with open(path, 'r') as handle:
            table=csv.reader(handle, delimiter="\t")
            df=pd.DataFrame(table)
            new_header = df.iloc[0]
            df_head = df[1:]
            df_head.columns = new_header
            
            """Variance"""
            
            df_var=df_head.drop("strain", 1)
            df_var2=df_var.astype(float)
            var2=[]

            
            for i in df_var2.columns:
                j=df_var2.var()[i]
                var2.append(j)
            
            """difference"""
            diff=[]
            
            df_var2_arr=df_var2.to_numpy()
            df_var3=df_var2_arr.T
            wt=df_var2_arr[0]

            gene_diff=[]

            
            
            for i in range(0,len(wt)):
                d=abs(df_var3[i]-wt[i])
                gene_diff.append(d)

            gene_diff_pd1=pd.DataFrame(gene_diff)
            gene_diff_pd=gene_diff_pd1.T
            
            gene_diff_arr=gene_diff_pd1.to_numpy()

            gene_var_division=[]
            for i in range(0,len(var2)):
                dd=gene_diff_arr[i]/math.sqrt(var2[i])
                gene_var_division.append(dd)
            gene_pd=pd.DataFrame(gene_var_division)
            gene_pd=gene_pd.T
            
            cdf=stats.norm.cdf(gene_pd)
            
            final=(2*cdf)-1
            final_df=pd.DataFrame(final)
            
            new_header_2 = df.iloc[0]
            final_df.columns=new_header_2[1:]

            first_col=pd.DataFrame(df_head["strain"])
            first_col.reset_index(inplace=True)
            first_col_2=first_col.drop(columns="index")
            final_df=pd.concat([first_col_2["strain"], final_df], axis=1)
            final_df_3 = final_df.drop(final_df.index[[0]])
            final_df_3.reset_index(inplace=True)
            final_df_4=final_df_3.drop(columns="index")

            final_df_5 = final_df_4.drop(columns="strain")

            col_names1=new_header_2[1:]
            col_names=col_names1.to_numpy()
            

            row_names1 = final_df_4["strain"]
            row_names=row_names1.to_numpy()
            
            empty=[]
            
            ff = list(final_df_4)

            stdoutOrigin=sys.stdout 
            sys.stdout = open("log2.txt", "w")

            for i in range(0, len(col_names)):
                for j in ff:

                    
                    print(j,final_df_4[j][i])

            sys.stdout.close()
            sys.stdout=stdoutOrigin
                    
                    
                        
                            

                