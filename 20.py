#!/Users/Jude-KSH/mystuff python  
#coding:utf-8  

from sys import argv ##从sys中导入argv

script, input_file = argv	##解包

def print_all(f):			##定义函数
	print (f.read())		##函数内容：f需要重点解释
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file)

print("first let us print the whole file:\n")

print_all(current_file)

print("now let us rewind, kind of like a tape.")

rewind(current_file)

print("let us print three lines:")

current_line = 1  #需要给 current_line赋初始值
print_a_line(current_line, current_file)

current_line += 1 #current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1 #current_line = current_line + 1
print_a_line(current_line, current_file)