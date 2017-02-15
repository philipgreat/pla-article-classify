# encoding=utf-8
import jieba
import os

def gen_idf_for_one_file(source_file_path,dest_file_path):

    sourcefile = open(source_file_path,"r") 
    content = sourcefile.read()
    seg_list = jieba.cut(content, cut_all=False)
    destfile = open(dest_file_path,"w")
    destfile.write(u"\n".join(seg_list).encode("utf-8"))

#cut_one_file("data/army/1.txt","data/army/1.keyword")

for (cur, dirs, files) in os.walk('data'):
    depth = len(cur.split('/'))
    #print "--" * depth, cur
    for fname in files:
        if(fname.endswith(".txt")):
            print cur+"/"+ fname
            source_file_name = cur+"/"+ fname
            dest_file_name = cur+"/"+ fname+".idf"
            gen_idf_for_one_file(source_file_name,dest_file_name)

            