formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter %
	("I had this thing.", #这里括号一定要加
	"That you could type up right.",
	"but it didnt sing.",
	"so i said goodnight."))