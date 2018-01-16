#!/Users/Jude-KSH/mystuff python  
#coding:utf-8  

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("你有 %d 块奶酪" % cheese_count)
	print("你有 %d 个盒子" % boxes_of_crackers)
	print("够吃了")
	print("get a blanket. \n")
	

print("可以直接这样表示：")
cheese_and_crackers(20, 30)


print("或者，我们可以这样写")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print ("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("我们可以把这两种合起来")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)