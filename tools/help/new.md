``` json
{
	"new": {
		"filedir": "",
		"filename": "newCommandOrNotes.py",
		"commandName": "new",
		"commandArguments": "cf",
		"testFilename": "",
		"description": "new.md"
	}
}
```

new

新建 command：`new -c [commandName] {-f [filename]}`
注：这里的filename不用加扩展名，默认就是.py

前置：
1. 如果没有filename，则默认 filename=commandName+'.py'
2. 检测是否存在该命令，是否存在该filename

动作：
1. 在 register_command.json 中注册
2. 新建对应的代码文件
3. 新建对应的描述文件

