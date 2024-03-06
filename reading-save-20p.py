#!/usr/bin/env python3

######### READ THE FOLLOWING INSTRUCTIONS BEFORE RUNNING SCRIPT #########
###                                                                   ###
### Description: This script was created for reading vibration files  ###
###              with values in their columns. It then generates a    ###
###              final file with one column from each file, where     ###
###              each column contains information about the vibration ###
###              mode.                                                ###
###                                                                   ###
###                                                                   ###
###                                                                   ###
###                                                                   ###
### Format running: python3 reading-save-v2.py                        ###
###                                                                   ###
###                                                                   ###
###                                                                   ###
### Format of the code: This script reads 1063 files, each containg 3 ###
###                     columns. The files are named Tper_i.csv, where###
###                     i represents the loop value. After reading,   ###
###                     the script organizes the columns into an      ###
###                     established array and saves the information   ###
###                     in the Tperc_final.csv  file.                 ###
###                                                                   ###
###                                                                   ###
#########################################################################


import numpy as np
import os
import csv
import pandas as pd
atom = "V1"
vibra_name = "V2"
df1 = pd.DataFrame()
for i in range(1,1063):
   # n = 1
    file_name = f"Tperc_{i}.csv"
    df = pd.read_csv(file_name)  
    if i > 0:
        column_cero = "Column_0"
        column_atom = df[atom].values
        column_name = f"Column_{i}"
        column_vibra = df[vibra_name].values
        column_vibra[np.isnan(column_vibra)] = -1
        df1[column_cero] = column_atom
        df1[column_name] = column_vibra
        mask = df1[column_name] < 0.6
        df1.loc[mask,column_name] = -2        
        del column_vibra
    #    n += 1
        csv_file_path = "Tperc_final_4.csv"
        df1.to_csv(csv_file_path)
      
       
