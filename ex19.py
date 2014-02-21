def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

def myfunc(argv, argv2):
	print "%d + %d is %d" % (argv, argv2, argv+argv2)

myfunc(1, 2)
a = 5
b = 6
myfunc(a, b)
myfunc(a+2, b+3)
myfunc(a*b, a/b)
myfunc(a-b, a+b)
myfunc(3+2, 5*2)
c = raw_input("input a number: ")
d = raw_input("input another number: ")
myfunc(int(c), int(d)) # must use int(c) not c!!!! c is string