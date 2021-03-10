'''
将'# '式改为'region'式
'''

import re

with open('t.md', 'r', encoding='utf-8') as f:
	lines = f.readlines()
	while(lines[0]=='\n'):
		lines = lines[1:]
	while(lines[-1]=='\n'):
		lines = lines[:-1]
	lines[-1] = lines[-1][:-1]

isEnd = [False] * 6
strings = ['topic', 'subtopic', 'h3', 'h4', 'h5', 'h6']

with open('v.md', 'w', encoding='utf-8') as f:
	for line in lines:
		if(re.match('[#]+ ', line)):
			num = len(re.match('[#]+ ', line).group()) - 2
			if(num>=6):
				f.write(line)
			else:
				if(isEnd[num]==True):
					isEnd[num]==False
					f.write('<!-- #endregion -->\n')
					f.write('<!-- #region --> ' + strings[num] + ': @ ' + line[num+2:])
				else:
					isEnd[num]=True
					f.write('<!-- #region --> ' + strings[num] + ': @ ' + line[num+2:])
		else:
			f.write(line)
	
	for i in range(0, 6):
		if(isEnd[i]==True):
			f.write("\n\n<!-- #endregion -->")
