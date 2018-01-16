#!/Users/Jude-KSH/mystuff python  
#coding:utf-8  

def add(a, b):
	print ("加法： %d + %d" % (a, b))
	return a + b

def substract(a, b):
	print ("减法： %d - %d" % (a, b))
	return a - b

def muiltyply(a, b):
	print ("乘法： %d * %d" % (a, b))
	return a * b
	
def divide(a, b):
	print ("除法： %d / %d" % (a, b))
	return a / b


print ('let us do some math with just function!')

age = add(20, 5)
height = substract(78, 4)
weight = muiltyply(90, 2)
iq = divide(100, 2)

print ("岁数： %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq))


#猜谜语
print ("here is a puzzle.")

what = add(age, substract(height, muiltyply(weight, divide(iq, 2))))

print ("that becomes:", what, "can you do it by hand?")