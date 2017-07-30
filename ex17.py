from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" %(from_file, to_file)

# we could do these two on one line too, how?

#in_file = open(from_file)
#indata = in_file.read()

#indata = open(from_file).read()


#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exists? %r" % exists(to_file)
#raw_input('Hit ENTER to copy file, CTRL+C to abort.')

#out_file = open(to_file, 'w')
#out_file.write(indata)

out_file = open(to_file, 'w').write(open(from_file).read())

print "Alright, all done!"

#out_file.close()