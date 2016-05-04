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
