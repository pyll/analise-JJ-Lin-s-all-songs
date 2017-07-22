import xlrd
import jieba
import numpy
import codecs
import pandas
# import matplotlib.pyplot as plt
# from wordcloud import wordcloud
file=codecs.open(r"歌词大全.txt",'r','utf-8')
content=file.read()
file.close()
segments=[]
segs=jieba.cut(content)
for seg in segs:
    if len(seg)>1:
        segments.append(seg)
segmentDF=pandas.DataFrame({'segment':segments})
df=segmentDF.groupby("segment")["segment"].agg({"计数":numpy.size})
print(df.head(100))
df.to_excel(r'ljj.xls',sheet_name 'sheet1')
