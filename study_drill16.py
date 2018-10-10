from sys import argv

script, filename = argv

txt = open(filename)

print "Here is a new script %r." % filename



print txt.read()