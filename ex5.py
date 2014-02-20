name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = "White"
hair = 'Brown'

print "Let's talk about %s." % (name)
print "He's %d inches tall." % height
print "He's %d pounds heavy." %weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to  get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age+height+weight)

#format character %r: print this not matter what
print "character %r" % name  # ===>  character 'Zed A. Shaw'
print "character %r" % age  #  ===>  character 35

inches=3
pounds=180
print "%d pounds equal to %d kilos" % (pounds, round(0.45 * pounds))
print "%d inches equal to %f centimeters." % (inches, round(2.54 * inches))
print "%f" % round(3.49599, 2)
#round(3.5) ==> 4.0  round(3.49999) ====> 3.0
#round(3.49999, 2) ==> 3.50