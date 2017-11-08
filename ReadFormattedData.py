# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 12:27:08 2017

@author: Administrator
"""
import pandas as pd

class ReadFormattedData:
    
    def __init__(self,filename):  
        self.__filename = filename  
        
    def execute(self):  
         df = pd.read_csv(self.__filename)
         return df


if __name__ == "__main__":
    d = ReadFormattedData("formatted_data.csv").execute()
