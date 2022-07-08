import re
import os
"""字符串列表根据标识符顺序有序提取相应数字
eg. 
	以sdf为顺序提取
	[s1d2f3]->[1,2,3]
	[d4s1f7]->[147]
	[s1f2]->[1,,2]"""
def orderString(object,patternlist0):#object：文件内容列表，orderlist0:筛选的文件内容列表，元素为每行提取内容
	orderList0 = []
	patternlist1 = []
	for p in patternlist0:
		p = re.compile(p)
		patternlist1.append(p)
	#判断类型
	if isinstance(object,list):
		for string in object:
			orderList1 = []
			for p in patternlist1:
				for i0 in p.findall(string):
					if type(i0)==list or type(i0)==tuple:
						i0 = map(int,i0)
						for i1 in i0:
							orderList1.append(i1)
					else:
						i0 = int(i0)
						orderList1.append(i0)
			if len(orderList1)!=0:
				orderList0.append(orderList1)
		# if len(orderList0)!=0:
		# 	print(orderList0)
	else:
		print("请输入列表")
	return orderList0
#路径筛选文件列表
def findNotDir(path):
	filelist = []
	files = os.listdir(path)
	for file in files:
		file = os.path.join(path,file)
		if not os.path.isdir(file):
			filelist.append(file)
	return filelist
#一个列表关键词出现总数
def sumKeyWord(lines,patternlist):
	wordnum = 0
	patternlist1 = []
	for p in patternlist:
		p = re.compile(p)
		patternlist1.append(p)
	for line in lines:
		for p in patternlist1:
			if p.findall(line):
				wordnum+=1
				print(line.rstrip())
	return wordnum
if __name__ == '__main__':
	x = ["a应该为1，b爷爷   续是2，c为3,a为9","b大概率是4，c为  8，a为3","f为4，d为1"]
	y = [r".*?a.*?(\d+).*?",r".*b.*?(\d+).*",r".*c.*?(\d+).*"]
	z = "a应该为1，b爷爷   续是2，c为3,a为9"
	print(orderString(x,y))
	orderString(z,y)