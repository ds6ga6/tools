'''
打开 haha.md，写入时间并编辑
'''

import time
import os
import re

FILENAME = 'source\\haha.md'
ENDLABEL = '【END】'

################################################################################
# 备份 FILENAME 为 .FILENAME
################################################################################

if(os.path.exists(FILENAME)):
	os.system('copy ' + FILENAME + ' .' + FILENAME)
else:
	with open(FILENAME, 'w', encoding='utf-8') as f:
		f.write('\n\n'+ENDLABEL)

################################################################################
# 打开 FILENAME 并在 ENDLABEL 前写入时间
################################################################################

with open(FILENAME, 'r', encoding='utf-8') as f:
	fdata = f.read()

# 获得当前时间
stmp = time.localtime() # 获得当前时间
datastring = time.strftime('%Y-%m-%d %H:%M:%S', stmp) # 输出格式为 @data: 0000-00-00 00:00:00
time = '@data:' + datastring + '\n'

# 分隔符
sech = '\n---\n\n'

fdata = fdata.replace('\n\n'+ENDLABEL, '\n\n'+sech+time+sech+'\n\n'+ENDLABEL)

with open(FILENAME, 'w', encoding='utf-8') as f:
	f.write(fdata)

################################################################################
# 用 typora 打开 FILENAME
################################################################################

os.system('start ' + FILENAME)