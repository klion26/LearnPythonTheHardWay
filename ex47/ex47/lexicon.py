def scan(par):
	direction = [('direction', 'north'),
					  ('direction', 'south'),
					  ('direction', 'east')]
	verbs = [('verb', 'go'),
					  ('verb', 'kill'),
					  ('verb', 'eat')]
	stops = [('stop', 'the'),
					  ('stop', 'in'),
					  ('stop', 'of')]
	nouns = [('noun', 'bear'),
					  ('noun', 'princess')]

	l = par.split()
	ret = []
	for i in l:
		if None != convert_number(i):
			ret.append(('number', convert_number(i)))
		else:
			used = True
			for t in direction:
				if i == t[1]:
					ret.append(t)
					used = False
					break
				else:
					pass
			for t in stops:
				if i == t[1]:
					ret.append(t)
					used = False
				else:
					pass
			for t in nouns:
				if i == t[1]:
					ret.append(t)
					used = False
				else:
					pass
			for t in verbs:
				if i == t[1]:
					ret.append(t)
					used = False
				else:
					pass
			if used:
				ret.append(("error", i))
	return ret

#convert s to int
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
