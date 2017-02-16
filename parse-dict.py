# encoding=utf-8
import jieba  
import jieba.analyse  
import math  

'''
从文件中得到向量
'''
def dict_from_file(file_path):
    dict = {}
    number = 1
    with open(file_path,'r') as inf:
        for line in inf:
            print str(number)+": "+line+" "
            (key, val) = line.strip().split(' ')
        #dict.append(eval(line)) 
            dict[key] = float(val)
            number +=1
            #
    return dict


dict_from_file("extradict/idf.txt")