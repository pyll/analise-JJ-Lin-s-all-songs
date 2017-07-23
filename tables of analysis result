#----the favorite season----
import numpy as np
import matplotlib.pyplot as plt

#设置画布大小，添加子图
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)

#标题
plt.title(u'最喜欢的季节',fontproperties='SimHei',fontsize=20)

#绘图数据
x=[1,2,3,4]
y=[1,10,2,3]
#柱图
plt.bar(x,y)
#y标签
plt.ylabel(u'出现次数',fontproperties='SimHei',fontsize=10)

#柱状图显示数值
for i in range(4):
    plt.text(x[i],y[i]+0.1,y[i])

#设置x轴刻度
ax.set_xticks([1,2,3,4])
ax.set_xticklabels([u'春天',u'夏天',u'秋天',u'冬天'],fontproperties='SimHei',fontsize=10)

plt.show()

#--------the favorite color--------
import numpy as np
import matplotlib.pyplot as plt

#设置画布大小，添加子图
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)

#标题
plt.title(u'最喜欢的颜色',fontproperties='SimHei',fontsize=20)

#柱图数据
x=[1,2,3,4,5,6,7,8,9,10]
y=[1,1,3,2,1,5,3,1,3,1]
#柱图
plt.bar(x,y,color=['silver','goldenrod','g','whitesmoke','y','k','r','lightgrey','b','skyblue'])
#y标签
plt.ylabel(u'出现次数',fontproperties='SimHei',fontsize=10)

#柱状图显示数值
for i in range(10):
    plt.text(x[i],y[i]+0.1,y[i])

#设置x轴刻度
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
ax.set_xticklabels([u'银色',u'琥珀色',u'绿色',u'白色',u'黄色',u'夜色',u'红色',u'银白色',u'蓝色',u'天色'],fontproperties='SimHei',fontsize=10)

plt.show()

#--------the songs' sentiment--------
import matplotlib.pyplot as plt
#标签
label='positive','negative','neutral'
#标签占比
sizes=[46,58,2]
#标签颜色
colors=['y','skyblue','g']
#标题
plt.title(u'歌曲的情感',fontproperties='SimHei',fontsize=20)
#饼图
plt.pie(sizes,labels=label,colors=colors,autopct='%1.1f%%',shadow=False,startangle=90)

plt.show()

#--------the day when JJ Lin lives---------
import numpy as np
import matplotlib.pyplot as plt

#设置画布大小，添加子图
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)

#标题
plt.title(u'林俊杰活在哪一天',fontproperties='SimHei',fontsize=20)

#绘图数据
x=[1,2,3,4,5]
y=[2,7,5,23,33]
#柱图
plt.bar(x,y,color='violet')
#y标签
plt.ylabel(u'出现次数',fontproperties='SimHei',fontsize=10)

#柱状图显示数值
for i in range(5):
    plt.text(x[i],y[i]+0.1,y[i])

#设置x轴刻度
ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels([u'那天',u'昨天',u'今天',u'明天',u'未来'],fontproperties='SimHei',fontsize=10)

#设置网格线
plt.grid( color='aqua',linestyle='--', linewidth=0.5 ,axis='y',alpha=0.3)

plt.show()
