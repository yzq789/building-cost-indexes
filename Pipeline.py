# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 12:29:16 2017

@author: Administrator
"""

class Pipeline:
    
    def __init__(self):
        self.operations = []
        
    def run(self):
        medium_res = None
        for operation in self.operations:
            if medium_res is None:
                medium_res = operation.execute()
            else:
                medium_res = operation.execute(medium_res)
        return medium_res
    
    def add(self, operation):
        self.operations.append(operation)
        return self
