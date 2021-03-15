# 把数转为二进制

import math

FRAC_MAX = 10 # 保留小数的位数

x = eval(input("请输入要转为二进制的数或表达式：\n"))

frac, inte = math.modf(x)

binary = bin(int(inte))[2:]

if(frac!=0):
	binary += '.'
	
	count = FRAC_MAX
	while(count!=0 and frac!=0):
		count -= 1
		frac *= 2
		if(frac>=1):
			frac -= 1
			binary += '1'
		else:
			binary += '0'

print(binary)