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
    sourcefile = open(file_path,"r") 
    content = sourcefile.read()
    #seg_list = jieba.cut(content, cut_all=False)
    tags = jieba.analyse.extract_tags(content,  topK=200, withWeight=True)
    for tag in tags:
        key_encoded = tag[0].encode("utf-8")
        dict[key_encoded] = tag[1] #string and flat pair
    return dict 



jieba.load_userdict("extradict/pla-dict.txt")
jieba.analyse.set_stop_words("extradict/stopwords")
#jieba.analyse.set_idf_path("extradict/idf.txt");

all_force=["army","navy","airforce","rocket"]
all_force_dict={}
'''
得到所有军种的向量
'''
for force in all_force:
    #print force
    all_force_dict[force] = dict_from_file("data/"+force+".tfidf")



'''
按照目标map的顺序构造数组，如果在相关分类中这个维度没有，则记为0
'''

def print_dict(dict):
     for key, value in dict.items():
         print key+": "+str(value)

def cos_test(dict_target,dict_one_force):
    vector_target = []
    vector_candidate = []
    for key, value in dict_one_force.items():
        #print "process key: "+key
        
        #key_encoded = key.decode("utf8")

       

        if  key in dict_target:
            target_value = dict_target[key]
            vector_target.append(target_value)
            vector_candidate.append(value)
            #print "should get here"
        
            #print key+"\t"+str(value)+"\t" + str(target_value)


    return cos_dist(vector_target,vector_candidate)
    #return cos_dist(vector_candidate,vector_target)
    
'''
def cos_test2(dict_target,dict_one_force):
    vector_target = []
    vector_candidate = []
    for key, value in dict_target.items():
        #print "process key: "+key
        vector_target.append(value)
        #key_encoded = key.decode("utf8")
        if  key in dict_one_force:
            vector_candidate.append(dict_one_force[key])
            #print "should get here"
            #print key+": "+str(value)+ str(dict_one_force[key])
        else:
            #print "s-----"
            vector_candidate.append(0)

    return cos_dist(vector_target,vector_candidate)
'''


def find_max_key(dict):
    candidate_key=""
    current_max_value = 0.0 # for positive values only
    for key, value in dict.items():
        if value > current_max_value :
            current_max_value =   value  
            candidate_key = key
    return candidate_key


def find_min_key(dict):
    candidate_key=""
    current_min_value = 100000000.0 # for positive values only
    for key, value in dict.items():
        if value < current_min_value :
            current_min_value =   value  
            candidate_key = key
    return candidate_key

#v1 = all_force_dict["navy"]


'''
得到目标文章的向量
'''

def test_article(target_path,all_force_vector):
    result_map={}
    target_map = dict_from_content(target_path)
    for key, value in all_force_vector.items():
        result = cos_test(target_map,value)
        result_map [key] = result
        print "The cosin value is "+ str(result)+" for "+key
    type_of_force = find_max_key(result_map)
    print "The max value shows the article '"+target_path+"' classify result is: "+type_of_force

    type_of_force = find_min_key(result_map)
    print "The min value shows the article '"+target_path+"' classify result is: "+type_of_force


    return type_of_force

def test(target_path):
    return test_article(target_path,all_force_dict)


test("data/navitest.txt")
test("data/armytest.txt")
test("data/airforcetest.txt")
test("data/rockettest.txt")


'''


target_file_path = "data/navitest.txt"

target_map = dict_from_content(target_file_path)

result_map={}

for force in all_force:
    result = cos_test(target_map,all_force_dict[force])
    print ("the result is: "+ str(result)+" for "+force)
    result_map [force] = result

type_of_force = find_min_key(result_map)

print "the min value shows the result is: "+type_of_force



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










