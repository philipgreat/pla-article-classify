# encoding=utf-8
import jieba
import os
import jieba.analyse
import sys

reload(sys)
sys.setdefaultencoding("utf8")
import math

 
def cos_dist(a, b):
    if len(a) != len(b):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for a1, b1 in zip(a,b):
        part_up += a1*b1
        a_sq += a1**2
        b_sq += b1**2
    part_down = math.sqrt(a_sq*b_sq)
    if part_down == 0.0:
        print "here?"
        return None
    else:
        return part_up / part_down

'''
从文件中得到向量
'''
def dict_from_file(file_path):
    dict = {}
    with open(file_path,'r') as inf:
        for line in inf:
            (key, val) = line.split()
        #dict.append(eval(line)) 
            dict[key] = float(val)
            #print key+": "+val
    return dict

def dict_from_content(file_path):
    dict = {}
    sourcefile = open(target_file_path,"r") 
    content = sourcefile.read()
    #seg_list = jieba.cut(content, cut_all=False)
    tags = jieba.analyse.extract_tags(content,  topK=200, withWeight=True)
    for tag in tags:
        dict[tag[0]] = tag[1] #string and flat pair
    return dict 





all_force=["army","navy","airforce","rocket"]
all_force_dict={}
'''
得到所有军种的向量
'''
for force in all_force:
    #print force
    all_force_dict[force] = dict_from_file("data/"+force+".tfidf")

'''
得到目标文章的向量
'''

target_file_path = "data/navitest.txt"

target_map = dict_from_content(target_file_path)

'''
按照目标map的顺序构造数组，如果在相关分类中这个维度没有，则记为0

'''

def print_dict(dict):
     for key, value in dict.items():
         print key+": "+str(value)

def cos_test(dict_target,dict_one_force):
    vector_target = []
    vector_candidate = []
    for key, value in dict_target.items():
        
        vector_target.append(value)
        key_encoded = key.encode("utf8")
        if  key_encoded in dict_one_force:
            vector_candidate.append(dict_one_force[key_encoded])
            #print "should get here"
            #print key+": "+str(value)+ str(dict_one_force[key.encode("utf8")])
        else:
            #print "s-----"
            vector_candidate.append(1)



    return cos_dist(vector_target,vector_candidate)

def find_min_key(dict):
    candidate_key=""
    current_min_value = 1000000000.0 # for positive values only
    for key, value in dict.items():
        if value < current_min_value :
            current_min_value =   value  
            candidate_key = key
    return candidate_key

#v1 = all_force_dict["navy"]

result_map={}

for force in all_force:
    result = cos_test(target_map,all_force_dict[force])
    print ("the result is: "+ str(result)+" for "+force)
    result_map [force] = result

type_of_force = find_min_key(result_map)

print "the result is: "+type_of_force




'''

print_dict(all_force_dict["navy"])

print "---------------------------------------------------------------"

print_dict(target_map)


d = {}
with open("file.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val

target_file_path = "data/navitest.txt"
sourcefile = open(target_file_path,"r") 
content = sourcefile.read()
    #seg_list = jieba.cut(content, cut_all=False)
target_tags = jieba.analyse.extract_tags(content,  topK=50, withWeight=True)

all_force=["army","navy","airforce","rocket"]

force_vector = list()


for force in all_force:
    print force
    force_vector
    #gen_tfidf_for_one_file("data/"+force+"/"+force+".txt","data/"+force+"/"+force+".tf


'''










