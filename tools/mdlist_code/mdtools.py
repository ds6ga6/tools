# 提取出 markdown 有序列表的中间几个层级

import copy
import re

# denpency import
import tools

# denpency macro
SIGN_INDENT	= '  '	# mdlist前面的缩进符号，有的是'\t'，有的是'  '
SIGN_FEED	= '\n'	# 换行符号
LIST_SIGN	= '([0-9]{1,2}\.|-) '	# 正则表达式下的序列符号

# 以树的结构保存 md有序列表
class mdTree():
	def __init__(self, text="", children=[]):
		# text 用来保存列表中每个节点上的内容
		self.text = text
		# children 作为列表保存多个 mdTree
		self.children = children

# mdcontext	: 输入的 md 内容，可以是 str、list、nlists、mdtree 4种形式
# type_d	: 目标类型，同样可以是 nlists、mdtree 2种形式
# （str、list的输出形式较为丰富，另用专门的函数转换）
def changeMdType(context_s, type_d):
	# 根据 context_s 得到输入的类型
	if(type(context_s) == str):
		type_s = 'str'
	elif(type(context_s) == mdTree):
		type_s = 'mdtree'
	elif(type(context_s) == list):
		if(len(context_s) == 0):
			tools.printInColor('Error: input context_s is null', 'red')
			exit(1)
		if(type(context_s[0]) == tuple):
			type_s = 'nlists'
		elif(type(context_s[0]) == str):
			type_s = 'list'
		else:
			tools.printInColor('Error: invaild source type', 'red')
			exit(1)
	else:
		tools.printInColor('Error: invaild source type', 'red')
		exit(1)
	
	# 检查 type_d
	typeset = set('nlists', 'mdtree')
	if(type_d not in typeset):
		tools.printInColor('Error: invaild type_d', 'red')
		exit(1)

	# lines -> nlists=[(n, text), ...] n是层数
	def lines_to_nlists(lines):
		nlists = []
		for line in lines:
			assert re.match("("+SIGN_INDENT+")*"+LIST_SIGN, line)
			count = 0	# 没有缩进的层数为1，认为“工作指针”或根结点处是0
			while(re.match(SIGN_INDENT, line)):
				line = line.replace(SIGN_INDENT, '', 1)
				count += 1
			nlists.append((count, line))
		return nlists

	# nlist -> mdTree
	def nlists_to_mdtree(nlists):
		points = [mdTree()]
		layer = 0
		for nlist in nlists:
			assert nlist[0] <= layer + 1	# 否则就存在连续缩进，或说是空层
			if(len(points) == nlist[0]):	# 新建 mdTree 节点
				points.append(mdTree(nlist[1]))
			else:
				points[nlist[0]] = mdTree(nlist[1])
			points[nlist[0]-1].children.append(points[nlist[0]])	# 把 child 的指针给 parent
		return mdtree

	# mdTree -> nlists
	def mdtree_to_nlists(mdtree):
		nlists = []
		points = [(mdtree, 0)]
		while(points != []):
			point = points[-1][0]
			num = points[-1][1]
			if(len(point.children) > num):	# 还有child没遍历
				points.append((point.children[num], 0))	# 去遍历child
				points[-2] = (point, num+1)				# 更新节点的计数
			else:							# 当前节点的child遍历完了
				points = points[:-1]					# 删掉最后的节点
		return nlists
		
	# 4*2共8种情况
	if(type_s == 'str'):
		if(type_d == 'nlists'):
			lines = context_s.split(SIGN_FEED)
			nlists = lines_to_nlists(lines)
			return nlists
		elif(type_d == 'mdtree'):
			lines = context_s.split(SIGN_FEED)
			nlists = lines_to_nlists(lines)
			mdtree = nlists_to_mdtree(nlists)
			return mdtree
	elif(type_s == 'list'):
		if(type_d == 'nlists'):
			nlists = lines_to_nlists(context_s)
			return nlists
		elif(type_d == 'mdtree'):
			nlists = lines_to_nlists(context_s)
			mdtree = nlists_to_mdtree(nlists)
			return mdtree
	elif(type_s == 'nlists'):
		if(type_d == 'nlists'):
			return context_s
		elif(type_d == 'mdtree'):
			mdtree = nlists_to_mdtree(context_s)
			return mdtree
	elif(type_s == 'mdtree'):
		if(type_d == 'nlists'):
			nlists = mdtree_to_nlists(context_s)
			return nlists
		elif(type_d == 'mdtree'):
			return context_s


class Mdtools():
	def __init__(self, argv):
		pass