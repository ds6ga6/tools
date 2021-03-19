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

with open(REGISTER_FILELOAD, 'r', encoding='utf-8') as f:
	data = json.load(f)
commandDict = {}
for commandName in data.keys():
	commandDict[commandName] = data[commandName]['filename']

def exec_command(command):
	commandsplit = command.split(' ', 1)
	if(commandsplit[0] in commandDict.keys()):
		new_command = 'python ' + CODE_LOAD + commandDict[commandsplit[0]] + ' ' + commandsplit[1]
		print(new_command)
		os.system(new_command)
	else:
		os.system(command)

# 对 main.md
if(args['relativeFile']=='main.md'):
	with open(args['relativeFile'], 'r', encoding='utf-8') as f:
		command = f.readlines()[args['lineNumber']-1]
	exec_command(command)
# 对其他文件
else:
	print("相应功能正在开发中")