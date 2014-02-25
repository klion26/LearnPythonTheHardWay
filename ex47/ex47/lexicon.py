import re

def scan(par):
	direction = ['north', 'south', 'west', 'east', 'left', 'right',
			     'down', 'up', 'back']
	verbs = ['go', 'kill', 'stop', 'eat']
	stops = ['the', 'in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']
	
	words = par.split(' ')
	pattern = re.compile(r'\d+')

	ret = []
	for word in words:
		num = pattern.match(word)
		if num:
			sentence = ('number', convert_number(word))
			ret.append(sentence)
		elif word in direction:
			sentence = ('direction', word)
			ret.append(sentence)
		elif word in verbs:
			sentence = ('verb', word)
			ret.append(sentence)
		elif word in stops:
			sentence = ('stop', word)
			ret.append(sentence)
		elif word in nouns:
			sentence = ('noun', word)
			ret.append(sentence)
		else:
			sentence = ('error', word)
			ret.append(sentence)
	return ret

#convert s to int
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
