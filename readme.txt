目标： 给定一篇文章，找出这个文章属于哪个栏目

算法：

1. 找到分好类的文章 （400篇，4个类别,）

2. 对所有文章进行分词，可以用到专用词字典和停用词字典，生成400个文件

3. 利用这400个分词文件生成领域专用IDF文件，参照

http://blog.csdn.net/yan456jie/article/details/52078273

4. 将每个类别的100篇文章合并，运行TFIDF，各取top 50的关键词和权重，获得4个50维度的矢量，
每个矢量代表一个类别 V1~V4



5. 将一篇测试文件分词，统计每个类别的关键词出现频率，获得4个50维度的矢量

6. 计算每个类别的两个矢量差，获得最小的一个，如果它小于阈值，测试文章即该类别，如果大于则文章分类失败

第5步自己统计词频也可以，省事点可以先跑TFIDF, 取top 100或200，让后挑出类别关键词的那50个


最终执行结果：

The angle for navy is 0.714161202833
The angle for airforce is 0.781578682536
The angle for rocket is 0.779786047846
The angle for army is 0.780766596164
The min value shows the article 'data/navitest.txt' classify result is: navy
The angle for navy is 0.824570717524
The angle for airforce is 0.834250482476
The angle for rocket is 0.79891007397
The angle for army is 0.744447443492
The min value shows the article 'data/armytest.txt' classify result is: army


经过人工调整后，目前文章分类的准确率是100%
