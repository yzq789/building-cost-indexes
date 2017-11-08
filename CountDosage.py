# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 12:12:45 2017

@author: Administrator
"""

class CountDosage:

    def __init__(self, tatal_area):  
        self.tatal_area = tatal_area
        
    def execute(self, data_map):
        for key in data_map:
            data_map[key]["dosage_per_m2"] = data_map[key]["dosage"]/self.tatal_area;
        return data_map
        
        