#!/usr/bin/python
# -*-coding:utf-8 -*

from classes import *
from data import *

partis = {key:Parti(*parti) for key, parti in partisData.items()}
candidates = {key:Candidate(*candidate) for key, candidate in candidatesData.items()}

print partis
print candidates
