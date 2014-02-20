# set x
x = "There are %d types of people." % 10
# set binary
binary = "binary"
# se do_not
do_not = "don't"
# set y
y = "Those who know %s and Those who %s." % (binary, do_not)
# print x
print x
# print y
print y

print "I said: %r." % x
print "I also said: '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."
print #print a empty line
#print w+e (append)
print w + e