# new.md

import sys
import os
import json

REGISTER_FILELOAD = 'tools/config/register_command.json'
MD_LOAD = 'tools/.source/'
BACKUP_LOAD = 'tools/.source/backup/'
CODE_LOAD = 'tools/code/'

def printInColor(text, color):
	colorDict = {
		'black'		: '30',
		'red'		: '31',
		'green'		: '32',
		'yellow'	: '33',
		'blue'		: '34',
		'purple'	: '35',
		'white'		: '37',
		'default'	: '38'
	}
	print("\033[" + colorDict[color] + "m" + text + "\033[0m")

def writeSecure(text, fileload):
	with open(fileload, 'r', encoding='utf-8') as f:
		data = f.read()
	with open(BACKUP_LOAD + fileload.split('/')[-1], 'w', encoding='utf-8') as f:
		f.write(data)
	with open(fileload, 'w', encoding='utf-8') as f:
		f.write(text)

def newCommandOrNotes(arg):
	if('c' in arg.keys()):
		# 参数赋值
		commandName = arg['c']
		if('f' in arg.keys()):
			assert len(arg) == 2
			filename = arg['f']
		else:
			assert len(arg) == 1
			filename = commandName + '.py'
		
		# 检测是否存在该命令
		with open(REGISTER_FILELOAD, 'r', encoding='utf-8') as f:
			data = json.load(f).keys()
		if(commandName in data):
			printInColor("ERROR: the command is already exist!", 'red')
			exit()
		if(os.path.exists(filename)):
			printInColor("ERROR: the filename is already exist!", 'red')
			exit()
		
		# 在 register_command.json 中注册
		with open(REGISTER_FILELOAD, 'r', encoding='utf-8') as f:
			data_reg = json.load(f)
		data_reg[commandName] = {
			"filedir": "",
			"filename": filename,
			"commandName": commandName,
			"commandArguments": "",
			"testFilename": "",
			"description": commandName + '.md'
		}
		data = json.dumps(data_reg, ensure_ascii=False, indent='\t')
		writeSecure(data, REGISTER_FILELOAD)
		data_reg = json.dumps({commandName: data_reg[commandName]}, ensure_ascii=False, indent='\t') # 后面写入md
		
		# 新建对应的代码文件
		with open(CODE_LOAD + filename, 'w', encoding='utf-8') as f:
			f.write('# ' + commandName + '.md\n\n')
			f.write('def ' + filename.split('.')[0] + '(arg):\n\tpass\n\n')
			f.write("if(__name__=='__main__'):\n")
			f.write('\targ = {}\n')
			f.write('\tfor argvs in sys.argv[1:]:\n')
			f.write("\t\targv = argvs.split('=', 1)\n")
			f.write('\t\targ[argv[0]] = arg[argv[1]]\n')
			f.write('\tnewCommandOrNotes(arg)')
		
		# 新建对应的描述文件
		with open(MD_LOAD + commandName + '.md', 'w', encoding='utf-8') as f:
			f.write('``` json\n')
			f.write(data_reg + '\n')
			f.write('```\n\n')
			f.write(commandName + '\n\n')
		
	else:
		print('c not in arg')

if(__name__=='__main__'):
	arg = {}
	i = 1
	while(i < len(sys.argv)):
		assert sys.argv[i][0] == '-'
		assert i + 1 < len(sys.argv)
		arg[sys.argv[i][1:]] = sys.argv[i+1]
		i += 2
	newCommandOrNotes(arg)