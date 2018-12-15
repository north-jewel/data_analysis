from pyecharts import Bar
bar =Bar('我的第一个图表','这是副标题')
bar.add('题库',['判断题','填空题','多选题','简答题','选择题'],[3,15,2,5,2])
bar.render()
