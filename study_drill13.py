from sys import argv

script, user_name = argv
prompt = '>'

print "Hi! %s, I'm the %s script." % (user_name, script)
print "Can answer the following questions?"
print "How many classes does your school have %s?" % user_name
classes =int(raw_input(prompt))

print "And how many students?"
students = int(raw_input(prompt))

print """
So your school have %r classes.
And %r students.
""" % (classes, students)
