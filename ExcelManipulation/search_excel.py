#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:36:30 2020

@author: ioan
"""


import numpy as np
import pandas as pd

excel_file='Exemplu.xls'
sheet='sheet2'
df = pd.read_excel(excel_file, sheet)
print(df, "\n") # end= ' ', or "\n" are the same 


print(df['Name'].where(df['Occupation'] == 'Programmer'), "\n")
programmers = df['Name'].where(df['Occupation'] == 'Programmer')

print(programmers.dropna())

excel_files = ['Exemplu.xls', 'Exemplu2.xls', 'Exemplu3.xls']

for individual_excel in excel_files:
    df2 = pd.read_excel(individual_excel, sheet)
    print("\n", df2, "\n")
    
    programmerss = df2['Name'].where(df2['Occupation'] == 'Programmer')
    
    print(programmerss.dropna())
    
    
    
