#!/usr/bin/python
# -*-coding:utf-8 -*

from classes import *
from data import *
import random

partis = {key:Parti(key, *parti) for key, parti in partisData.items()}
candidates = {key:Candidate(key, partis, *candidate) for key, candidate in candidatesData.items()}

print "Partis: "
print "\t * " + "\n\t * ".join(partis.keys())
print "Candidates: "
print "\t * " + "\n\t * ".join(candidates.keys())

vote = Vote(candidates)

for i in range(1000):
    id_candidate = candidates.keys()[int(random.random() * len(candidates))]
    voter = Voter(i, candidates[id_candidate])
    voter.vote(vote)

print "Votes: "
max_votes = 0
winner = None
for k, nb_votes in vote.nb_votes.items():
    print "\t * " + k + ": " + str(nb_votes)
    if nb_votes > max_votes:
        max_votes = nb_votes
        winner = k

print "\nVictory of " + winner