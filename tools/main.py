import sys
import os
import json

REGISTER_FILELOAD = 'tools/config/register_command.json'
CODE_LOAD = 'tools/code/'

assert len(sys.argv) == 13
args = {
	"workspaceFolder"			: sys.argv[1],	#	/home/your-username/your-project
	"workspaceFolderBasename"	: sys.argv[2],	#	your-project
	"file"						: sys.argv[3],	#	/home/your-username/your-project/folder/file.ext
	"fileWorkspaceFolder"		: sys.argv[4],	#	/home/your-username/your-project
	"relativeFile"				: sys.argv[5],	#	folder/file.ext
	"relativeFileDirname"		: sys.argv[6],	#	folder
	"fileBasename"				: sys.argv[7],	#	file.ext
	"fileBasenameNoExtension"	: sys.argv[8],	#	file
	"fileDirname"				: sys.argv[9],	#	/home/your-username/your-project/folder
	"fileExtname"				: sys.argv[10],	#	.ext
	"lineNumber"				: int(sys.argv[11]),
	"pathSeparator"				: sys.argv[12]	#	/ on macOS or linux, \\ on Windows
}

# 读取登记过的命令列表，保存为以下形式：
# commandDict = {'commandName1':'filename1', 'commandName2':'filename2'}
with open(REGISTER_FILELOAD, 'r', encoding='utf-8') as f:
	data = json.load(f)
commandDict = {}
for commandName in data.keys():
	commandDict[commandName] = data[commandName]['filename']

# 执行命令
# commandType 代表要执行的命令的类型，比如 cmd, python, user(自定义的), ... 具体代码中会说明
# 如果类型是 'auto'。1. user; 2. cmd
def exec_command(command, commandType='auto'):
	if(commandType=='auto'):
		commandsplit = command.split(' ', 1)	# 取command最前面的字符串
		if(commandsplit[0] in commandDict.keys()):	# 成立代表是自定义的命令
			# 默认 python, 要用非 python 的要改这里
			new_command = 'python ' + CODE_LOAD + commandDict[commandsplit[0]] + ' ' + commandsplit[1]
			os.system(new_command)
		else:
			os.system(command)	# BUG 这里没有对命令是否是 cmd 命令做判断
	else:
		print("还不支持 auto 之外的命令")
		pass
	

# 对 main.md
if(args['relativeFile']=='main.md'):
	# 打开命令，并读取对应的行
	with open(args['relativeFile'], 'r', encoding='utf-8') as f:
		command = f.readlines()[args['lineNumber']-1]
	# 判断是否是 inline command, 如果是就切出来
	if(command.count('`')>=2):
		command = command.split('`', 2)[1]
	exec_command(command)
# 对其他文件
else:
	print("相应功能正在开发中")