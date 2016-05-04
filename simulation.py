#!/usr/bin/python
# -*-coding:utf-8 -*

class Common:
	def __init__(self, name, _type, typeName):
		self.name = name
		self.type = _type
		self.typeName = typeName

	def __str__(self):
		return "%s %s" % (self.typeName, self.name)

	def __repr__(self):
		return "%s %s" % (self.typeName, self.name)

	def __unicode__(self):
		return "%s %s" % (self.typeName, self.name)

class Parti(Common):
	def __init__(self, name):
		Common.__init__(self, name, "parti", "Parti")

class Candidate(Common):
	def __init__(self, name, parti=None):
		Common.__init__(self, name, "candidate", "Candidate")
		self.parti = parti

class Voter:
	def __init__(self, index, penchant):
		self.index = index
		self.penchant = penchant

	def vote(self, votingSystem):
		pass

partisData = {
	'extremeLeftWing': ['Extreme left'],
	'leftWing': ['Left'],
	'center': ['Center'],
	'rightWing': ['Right'],
	'extremeRightWing': ['Extreme right'],
}

partis = {key:Parti(*parti) for key, parti in partisData.items()}

candidatesData = {
	'Bob': ['Bob', partis['extremeRightWing']],
	'Lili': ['Lili', partis['leftWing']],
	'Jack': ['Jack', partis['center']],
	'Francis': ['Francis', partis['center']],
	'Lea': ['Lea', partis['rightWing']],
	'Jane': ['Jane', partis['extremeRightWing']],
}

candidates = {key:Candidate(*candidate) for key, candidate in candidatesData.items()}
print partis
print candidates
