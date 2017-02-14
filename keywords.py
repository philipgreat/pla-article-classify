# encoding=utf-8
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser#引入关键词的包
from docopt import docopt
data_path = "C:\\Users\\wangyuguang\\Desktop\\work_data\\profect_world\\"
topK = 10
withWeight = False
content = ""
for i in range(1,2):
    Data_path = data_path + "he"+".txt"
    content ="".join(open(Data_path, 'rb').read())
# print content
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)#直接调用

if withWeight is True:
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
else:
    print(",".join(tags))