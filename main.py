'''
参考：https://www.runoob.com/python/python-gui-tkinter.html
'''

# Python2.x 导入方法
from tkinter import *           # 导入 Tkinter 库
# Python3.x 导入方法
#from tkinter import *
root = Tk()                     # 创建窗口对象的背景色
# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']

listb = Listbox(root)  # 创建两个列表组件

for item in li:                 # 第一个小部件插入数据
    listb.insert(0, item)


listb.pack()                    # 将小部件放置到主窗口中

root.mainloop()                 # 进入消息循环
