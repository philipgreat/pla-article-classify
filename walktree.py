
# encoding=utf-8
import os
for (cur, dirs, files) in os.walk('data'):
    depth = len(cur.split('/'))
    #print "--" * depth, cur
    for fname in files:
        if(fname.endswith(".txt")):
            #print "--" * (depth + 1), fname, cur
            #print cur+"/"+ fname

            

