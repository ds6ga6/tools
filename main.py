'''
创建新笔记，影响
1. md_notes/ 下
2. xx.md
'''

import time
import os

stmp = time.localtime() # 获得当前时间
datastring = time.strftime('%Y-%m-%d %H:%M:%S', stmp) # 输出格式为 @data: 0000-00-00 00:00:00
xxname = time.strftime('%m.md', stmp)

if(os.listdir('md_notes')!=[]):
	old_filename = os.listdir('md_notes')[-1]
	id = int(old_filename[:3]) + 1
	old_name1 = old_filename[3:-3]
	# 对比上次的 topic_name 是否修改
	temp_name1 = 'md_notes\\' + old_filename
	with open(temp_name1, 'r', encoding='utf-8') as f:
		old_name2 = f.readline()[8:-1]
	if(old_name1!=old_name2):
		temp_name2 = 'md_notes\\' + old_filename[:3] + old_name2 + '.md'
		# 改 xx.md 中的内容
		temp_str1 = '[' + old_name1 + '](' + temp_name1 + ')'
		temp_str2 = '[' + old_name2 + '](' + temp_name2 + ')'
		with open(xxname, 'r', encoding='utf-8') as f:
			xxdata = f.read()
		xxdata = xxdata.replace(temp_str1, temp_str2)
		with open(xxname, 'w', encoding='utf-8') as f:
			f.write(xxdata)
		# 改文件名
		os.rename(temp_name1, temp_name2)
else:
	id = 0

topic_name = input("NAME IS : ")
topic_filename = 'md_notes\\' + '%03d' % id + topic_name + '.md' # 完整的相对路径

# 将这次的 topic 加入到 xx.md 中

with open(xxname, 'r', encoding='utf-8') as f:
	xxdata = f.read()

xxtemp = datastring + ' | [' + topic_name + '](' + topic_filename + ')'
xxdata = xxdata.replace('\n【XX END】', '\n' + xxtemp + '\n【XX END】')

with open(xxname, 'w', encoding='utf-8') as f:
	f.write(xxdata)

# 在 md_notes 中创建这次的 topic_file 并用typora打开

with open(topic_filename, 'w', encoding='utf-8') as f:
	f.write('@topic: ' + topic_name + '\n')
	f.write('@data:' + datastring + '\n')
	f.write('\n---\n\n')

os.system('start ' + topic_filename)

pass