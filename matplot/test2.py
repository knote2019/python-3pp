from matplotlib import pyplot as plot

#添加图形对象
fig = plot.figure()
ax = fig.add_axes([0, 0, 1, 1])

#使得X/Y轴的间距相等
ax.axis('equal')

#准备数据
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 12]

#绘制饼状图
ax.pie(students, labels=langs, autopct='%1.2f%%')
plot.show()
