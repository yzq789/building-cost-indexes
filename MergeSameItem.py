# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 12:27:57 2017

@author: Administrator
"""

class MergeSameItem:
        
    def execute(self,data):
        res = {}
        for i in range(0, len(data)):
            key = data.iloc[i,0]
            if res.has_key(key):
                if(data.iloc[i,2] > 0 and data.iloc[i,4] > 0):
                    res[key]["dosage"] += data.iloc[i,2]
                    res[key]["tatal_price"] += data.iloc[i,4]
            else:
                value = {"quantifier":data.iloc[i,1], "dosage":data.iloc[i,2], "price":data.iloc[i,3], "tatal_price":data.iloc[i,4]}
                res[key] = value
        return res
        
