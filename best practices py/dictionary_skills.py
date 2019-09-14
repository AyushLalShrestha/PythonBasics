#!/usr/bin/bash python
# source: https://youtu.be/OSGv2VnC0go

dictionary = {'ayyush': 518, 'anita': 219, 'astha': 22}
colors = ['red', 'blue', 'yellow']
color_codes = ['r', 'b', 'y']

#1. construct a dictionary from pairs
d1 = dict(izip(color_codes, colors))

#2. use defaultdict
d = defaultdict(int)
d['male'] += 1
d['female'] += 1

#3. use ChainMap
d2 = ChainMap(dict_1, dict_2, dict_3)