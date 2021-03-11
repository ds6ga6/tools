# 在每一行的开头依次添加 f(i), i从1开始, f可自己编辑
# 参考 "003文本添加序号小工具.md"

import tkinter as tk

class AddNumlist(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.grid()
		self.createWidget()

	def createWidget(self):
		# 控件初始化
		self.tb_content = tk.Text(self)
		self.tb_format = tk.Text(self)
		self.tb_format.insert('end', '%d. ')
		btn1 = tk.Button(self, text='转换', command=self.transfer)
		btn2 = tk.Button(self, text='退出', command=self.quit)

		# 控件加到 grid 里
		self.tb_content.grid(row=1, column=1, columnspan=2, sticky='W')
		self.tb_format.grid(row=2, column=1, columnspan=2, sticky='W')
		btn1.grid(row=3, column=1, sticky='W')
		btn2.grid(row=3, column=2, sticky='W')

		# 控件大小设置

	def transfer(self):
		lines = self.tb_content.get('0.0','end').split('\n')[:-1]
		forma = self.tb_format.get('0.0','end')
		for i in range(0, len(lines)):
			lines[i] = (forma % i)[:-1] + lines[i]
		# 刷新 text 的内容
		self.tb_content.delete('1.0','end')
		self.tb_content.insert('end', '\n'.join(lines))
		pass



app = AddNumlist()
app.master.title('文本添加序号小工具')
app.mainloop()