people = 30
cars = 40
buses = 15

if cars > people: #if cars > people
	print "We should take the cars."
elif cars < people: #if cars < people
	print "We should not take the cars."
else: #if cars == people
	print "We can't decide."

if (buses>cars): #if buses > cars
	print "That's too many buses."
elif buses < cars: #if buses < cars
	print "Maybe we could take the buses."
else: #if buses == cars
	print "We still can't decide."

if people > buses: # if people > buses
	print "Alright, let's just take the buses."
else: # if people <= buses
	print "Fine, let's stay home then."

if people < buses:
	if cars > buses:
		print "In"
else:
	print "Out 2"

if 40 > people> 20:# and people < 40:
	print "Between 20 and 40"