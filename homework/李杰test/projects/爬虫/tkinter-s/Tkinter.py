from tkinter import *

#创建窗口
root =Tk()

#窗口标题
root.title('网易云音乐')

#窗口大小
root.geometry('500x400+550+230')

#标签控件
label = Label(root,text='请输入要下载的歌曲')
label.grid()

#输入框
entry = Entry(root)





#显示窗口
root.mainloop()
