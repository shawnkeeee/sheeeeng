#this one is like your scripts with argv
def print_two(*args):
	argl, arg2 = args
	print ("argl: %r, arg2: %r" % (argl,arg2))
	
#ok,that *args is actually pointless, we can just do this 
def print_two_again(argl, arg2):
	print ('argl: %r, arg2: %r' % (argl, arg2))
	
#this just takes one arguments
def print_one(argl):
	print ('argl: %r' % argl)
	
#this one takes no arguments
def print_none():
	print ("i got nothin")
	
	
print_two("ke", "sheng")
print_two_again("ke", "sheng")
print_one("first!")
print_none()