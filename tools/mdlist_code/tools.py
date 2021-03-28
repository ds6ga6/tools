

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

def writeSecure(text, fileload, backupload='.source/.backup/'):
	with open(fileload, 'r', encoding='utf-8') as f:
		data = f.read()
	with open(backupload + fileload.split('/')[-1], 'w', encoding='utf-8') as f:
		f.write(data)
	with open(fileload, 'w', encoding='utf-8') as f:
		f.write(text)