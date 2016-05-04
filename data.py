#!/usr/bin/python
# -*-coding:utf-8 -*

import json

with open('partis.json') as data_file:  
    partisData = json.load(data_file)

with open('candidates.json') as data_file:    
    candidatesData = json.load(data_file)
