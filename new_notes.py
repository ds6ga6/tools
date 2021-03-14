'''
创建新笔记，影响
1. md_notes/ 下
2. xx.md
'''

GET_WORKSPACE_BY_GUI = False
xxLOAD = 'source\\'

workspace = ''
# workspace = '专用集成电路设计技术基础'
# workspace = '计算机组成与系统结构'
# workspace = '人工智能'
# workspace = '数字图像处理'
# workspace = '数字信号处理'
# workspace = '研究生相关'

import time
import os
import re

################################################################################
# 参考文档：002在gui中选择workspace与输入name.md
# 修改 GET_WORKSPACE_BY_GUI 来决定是否使用以下代码
################################################################################

import tkinter as tk

class InitTopic(tk.Frame):
	def __init__(self, workspaceList, master=None):
		super().__init__(master)
		self.workspaceList = workspaceList
		self.grid()
		self.createWidget()

	def createWidget(self):
		self.v = tk.StringVar()
		self.v.set(self.workspaceList[0])
		
		for i in range(0, len(self.workspaceList)):
			rbtn = tk.Radiobutton(self, text=workspaceList[i], value=workspaceList[i], variable=self.v)
			rbtn.grid(sticky='W')

		tk.Button(self, text='确定', command=self.confirm).grid(sticky='W')
	
	def confirm(self):
		self.workspace = self.v.get()
		self.quit()

if(GET_WORKSPACE_BY_GUI==True):
	workspaceList = [
		'无',
		'专用集成电路设计技术基础',
		'计算机组成与系统结构',
		'人工智能',
		'数字图像处理',
		'数字信号处理',
		'研究生相关'
	]

	initTopic = InitTopic(workspaceList)
	initTopic.master.title('init')
	initTopic.mainloop()

	workspace = initTopic.workspace

	if(workspace=='无'):
		workspace = ''

################################################################################

stmp = time.localtime() # 获得当前时间
datastring = time.strftime('%Y-%m-%d %H:%M:%S', stmp) # 输出格式为 @data: 0000-00-00 00:00:00
xxname = time.strftime('%m.md', stmp)

################################################################################
# 对比上次的 topic_name 是否修改
# 随便得到 id
################################################################################

if(os.listdir('md_notes')!=[]):
	old_filename = os.listdir('md_notes')[-1]
	id = int(old_filename[:3]) + 1
	old_name1 = old_filename[3:-3]
	# 对比上次的 topic_name 是否修改
	temp_name1 = 'md_notes\\' + old_filename
	with open(temp_name1, 'r', encoding='utf-8') as f:
		old_name2 = f.readline()[8:-1]
		# 去掉不能作为文件名的字符
		ban_character = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
		for ch in ban_character:
			old_name2 = old_name2.replace(ch, '')
	if(old_name1!=old_name2):
		temp_name2 = 'md_notes\\' + old_filename[:3] + old_name2 + '.md'
		# 改 xx.md 中的内容
		temp_str1 = '[' + old_name1 + '](' + temp_name1 + ')'
		temp_str2 = '[' + old_name2 + '](' + temp_name2 + ')'
		with open(xxLOAD + xxname, 'r', encoding='utf-8') as f:
			xxdata = f.read()
		xxdata = xxdata.replace(temp_str1, temp_str2)
		with open(xxLOAD + xxname, 'w', encoding='utf-8') as f:
			f.write(xxdata)
		# 改文件名
		os.rename(temp_name1, temp_name2)
else:
	id = 0

################################################################################

topic_name = input("NAME IS : ")

# 修复有时运行程序时莫名将 NAME 设为以下内容的 bug
while(topic_name=='C:/Users/11648/anaconda3/Scripts/activate'):
	topic_name = input("NAME IS : ")


topic_filename = 'md_notes\\' + '%03d' % id + topic_name + '.md' # 完整的相对路径

################################################################################
# 将这次的 topic 加入到 xx.md 中
################################################################################

with open(xxLOAD + xxname, 'r', encoding='utf-8') as f:
	xxdata = f.read()

xxtemp = datastring + ' | [' + topic_name + '](' + topic_filename + ')'
xxdata = xxdata.replace('\n【XX END】', '\n' + xxtemp + '\n【XX END】')

if(workspace!=''):
	wp = '【'+workspace+'】'
	if(re.search('\n'+wp, xxdata)):
		xxdata = xxdata.replace('\n' + wp, '\n' + xxtemp + '\n' + wp)
	else:
		xxdata += '\n\n' + xxtemp + '\n' + wp
	

with open(xxLOAD + xxname, 'w', encoding='utf-8') as f:
	f.write(xxdata)

################################################################################
# 在 md_notes 中创建这次的 topic_file 并用typora打开
################################################################################

with open(topic_filename, 'w', encoding='utf-8') as f:
	f.write('@topic: ' + topic_name + '\n')
	f.write('@data:' + datastring + '\n')
	f.write('@keywords: \n')
	f.write('\n---\n\n')

os.system('start ' + topic_filename)

pass