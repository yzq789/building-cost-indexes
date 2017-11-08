# -*- coding: utf-8 -*-

import pandas as pd

class SortAndWriteFile:

    def __init__(self, filename):
        self.filename = filename
    
    def execute(self,data_map):
        arr = []
        for key in data_map:
            arr.append([key, data_map[key]["quantifier"], 
                        data_map[key]["dosage"], data_map[key]["price"], 
                        data_map[key]["tatal_price"],
                        data_map[key]["dosage_per_m2"]])

        df = pd.DataFrame(arr,columns=[u'名称及规格',u'单位',u'数量',u'市场价',u'合计',u'单位面积用量'])
        df.sort_values(u'合计',0,False,True)
        
        print "writing..."
        df.to_csv(self.filename,index=False, encoding='utf-8')
        