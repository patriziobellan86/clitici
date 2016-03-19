# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 02:16:42 2016

@author: Patrizio
"""


print "test"

filetmp="tempforpurificatore.tmp.txt"
filein='input.txt'

fileout='output_2.txt'


s=file(filetmp)
d=s.readlines()


i=file(filein)
i=i.readlines()
print len(i), len(d), len(i)<len(d)

o=file(fileout)
do=o.readlines()
print len(do)
