#!/usr/bin/python
# -*-coding:utf-8 -*

class Common:
    def __init__(self, key, name, _type, type_name):
        self.key = key
        self.name = name
        self.type = _type
        self.type_name = type_name

    def __str__(self):
        return "%s %s" % (self.type_name, self.name)

    def __repr__(self):
        return "%s %s" % (self.type_name, self.name)

    def __unicode__(self):
        return "%s %s" % (self.type_name, self.name)

class Parti(Common):
    def __init__(self, key, name):
        Common.__init__(self, key, name, "parti", "Parti")
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

class Candidate(Common):
    def __init__(self, key, partis, name, parti=None):
        Common.__init__(self, key, name, "candidate", "Candidate")
        self.parti = partis[parti]
        self.parti.add_candidate(self)

class Vote:
    def __init__(self, candidates):
        self.nb_votes = { key: 0 for key,_ in candidates.items() }

    def add_vote(self, candidate):
        self.nb_votes[candidate] += 1

class Voter:
    def __init__(self, index, penchant):
        self.index = index
        self.penchant = penchant
        
    def vote(self, voting_system):
        voting_system.add_vote(self.penchant.key)
