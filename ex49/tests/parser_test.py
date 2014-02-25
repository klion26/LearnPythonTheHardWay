from nose.tools import *
from ex49 import lexicon, parser

def test_parse_sentence():
	result = lexicon.scan("bear eat the princess")
	sen = parser.parse_sentence(result)
	#ok = parser.Sentence("bear","eat","princess")
	#assert_equal(sen, parser.Sentence("bear","eat","princess"))
	assert_equal(sen.subject, "bear")
	assert_equal(sen.verb, "eat")
	assert_equal(sen.object, "princess")

@raises(Exception)
def test_verbexception():
	result = lexicon.scan("bear the princess")
	sen = parser.parse_sentence(result)

@raises(Exception)
def test_objectexception():
	result = lexicon.scan("bear eat the the eat")
	sen = parser.parse_sentence(result)
#def test_sentence():

def test_match():
	result = lexicon.scan("bear eat the xxx eat ... bear")
	sen = parser.match(result, "noun")
	assert_equal(sen, ("noun", "bear"))
