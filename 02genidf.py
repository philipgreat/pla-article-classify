# encoding=utf-8
import jieba
import os
import jieba  
import jieba.analyse  
import math  
  

''''' 
计算得到idf文件 
求idf得步骤： 
1、对所有文档进行分词，去停用词，结果放入二维list，其中每个元素是set 
1、得到文档数目；生成所有词的set 
2、对每个词计算idf：idf = log(n / docs(w, D)) 
'''  
  
def load_data(path):  
    ''''' 
    加载数据，解析json格式 
    :param path: 
    :return: 
    '''  
    with open(path) as f:
        content = f.readlines()

    return content  
  
def seg(content, stopwords):  
    ''''' 
    分词并去除停用词 
    '''  
    segs = jieba.cut(content, cut_all=True)  
    segs = [w.encode('utf8') for w in list(segs)]# 特别注意此处转换  
  
    seg_set = set(set(segs) - set(stopwords))  
    return seg_set  
  
def docs(w, D):  
    c = 0  
    for d in D:  
        if w in d:  
            c = c + 1;  
    return c  
  
def save(idf_dict, path):  
    f = file(path, "a+")  
    f.truncate()  
    # write_list = []  
    for key in idf_dict.keys():  
        # write_list.append(str(key)+" "+str(idf_dict[key]))  
        f.write(str(key) + " " + str(idf_dict[key]) + "\n")  
    f.close()  
  
def compute_idf(tags_data, stopwords):  
    # 所有分词后文档  
    D = []  
    #所有词的set  
    W = set()  
    for i in range(len(tags_data)):  
        #新闻原始数据  
        prevue = tags_data[i]
        d = seg(prevue, stopwords)  
        D.append(d)  
        W = W | d  
    #计算idf  
    idf_dict = {}  
    n = len(W)  
    #idf = log(n / docs(w, D))  
    for w in list(W):  
        idf = math.log(n*1.0 / docs(w, D))  
        idf_dict[w] = idf  
    return idf_dict  
  
  
  
path = 'data/army/1.txt.kw'  
tags_data = load_data(path)  
 
stopwords = {}.fromkeys([ line.rstrip() for line in open("extradict/stopwords") ]) 


def gen_idf_for_one_file(source_file_path,dest_file_path):

    #sourcefile = open(source_file_path,"r") 
    tags_data = load_data(source_file_path) 
    idf_dict = compute_idf(tags_data, stopwords)  
    save(idf_dict, dest_file_path)  

#cut_one_file("data/army/1.txt","data/army/1.keyword")

for (cur, dirs, files) in os.walk('data'):
    depth = len(cur.split('/'))
    #print "--" * depth, cur
    for fname in files:
        if(fname.endswith(".kw")):
            print cur+"/"+ fname
            source_file_name = cur+"/"+ fname
            dest_file_name = cur+"/"+ fname+".idf"
            gen_idf_for_one_file(source_file_name,dest_file_name)

            