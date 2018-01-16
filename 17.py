from sys import argv #从sys中载入argv
from os.path import exists ##从os中载入exists

script, from_file, to_file = argv	##解包

print ("coping from %s to %s " % (from_file, to_file)) ##

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print ("the input file is %d bytes long" % len(indata))

print ("does the putput file exist? %r" % exists(to_file))
print ("ready, hit return to continue, ctrl-c to abort.")
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("alright, all done.")

out_file.close()
in_file.close()