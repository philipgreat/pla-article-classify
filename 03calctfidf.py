# encoding=utf-8
import jieba
import os
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding("utf8")


def gen_tfidf_for_one_file(source_file_path,dest_file_path):

    sourcefile = open(source_file_path,"r") 
    content = sourcefile.read()
    #seg_list = jieba.cut(content, cut_all=False)
    tags = jieba.analyse.extract_tags(content,  topK=200, withWeight=True)
    destfile = open(dest_file_path,"w")

    
    for tag in tags:
            #print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
            output = str(tag[0])+" "+str(tag[1])+"\n"
            #print(output.encode("utf-8"))
            destfile.write(output.encode("utf-8"))
    destfile.close()



jieba.load_userdict("extradict/pla-dict.txt")
jieba.analyse.set_stop_words("extradict/stopwords")
jieba.analyse.set_idf_path("extradict/idf.txt")

all_force=["army","navy","airforce","rocket"]


for force in all_force:
    
    gen_tfidf_for_one_file("data/"+force+"/"+force+".txt","data/"+force+".tfidf")  
    print force+"...done"

            