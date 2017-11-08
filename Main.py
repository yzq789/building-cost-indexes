# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 12:29:36 2017

@author: Administrator
"""
from Pipeline import Pipeline
from ReadFormattedData import ReadFormattedData
from SortAndWriteFile import SortAndWriteFile
from CountDosage import CountDosage
from MergeSameItem import MergeSameItem

if __name__ == "__main__":
    project_classes = ["dian_qi_gong_cheng","jian_zhu_gong_cheng", "she_bei_gong_cheng", "zhuang_shi_gong_cheng"]
    
    for project_class in project_classes:
        pipeline = Pipeline()
        pipeline  \
            .add(ReadFormattedData("./data/" + project_class + ".csv")) \
            .add(MergeSameItem()) \
            .add(CountDosage(12776)) \
            .add(SortAndWriteFile("./result/dosage_" + project_class + ".csv"))
        df = pipeline.run()

