'''
参考：http://www.chenxm.cc/article/220.html
'''

import os
import sys
import json

if(len(sys.argv)>1):
	out_filename = sys.argv[1]
else:
	out_filename = 'all_file.json'

def create_dict(dir_road):
	file_dict = {}
	# root 当前目录路径
	# dirs 当前路径下所有子目录
	# files 当前路径下所有非目录子文件
	for root, dirs, files in os.walk(dir_road):
		if(root==dir_road):
			p_dict = file_dict
		else:
			p_dict = file_dict
			for di in root.split(dir_road)[1].split('\\')[1:]:
				p_dict = p_dict[di]
		p_dict['file'] = files
		for di in dirs:
			p_dict[di] = {}
	return file_dict

file_dict = create_dict(__file__.rsplit('\\', 1)[0])
with open(out_filename, "w", encoding='utf-8') as f:
	json.dump(file_dict, f, indent='\t', ensure_ascii=False)
