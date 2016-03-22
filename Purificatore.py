# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 12:55:44 2016

@author: Patrizio


"""
from __future__ import unicode_literals

import codecs

from AnalizzatoreCli import AnalizzatoreCli
from AnalizzatoreApostrofo import AnalizzatoreApostrofo

import os

class Purificatore:
    def VERSION(self):
        return "0.6.b"
        
    def __init__(self, fileinput, fileoutput, elaboraClitico = True,
                                             eliminaApostrofo = True):
        self.eliminaApostrofo = eliminaApostrofo
        self.elaboraClitico = elaboraClitico
        self.__ElaboraDati(fileinput, fileoutput)
        
        
    def __ElaboraApostrofo(self, fileinput, fileoutput):
        try:
            os.remove(fileoutput)
        except:
            pass
        
        obj=AnalizzatoreApostrofo()
        try:
            with codecs.open(fileinput, 'r', 'utf-8') as fin:                
                with codecs.open(fileoutput, 'a','utf-8') as fout:
                    for line in fin:
                        line=self.__SeparaColonne(line)
                        
                        dati=obj.AnalizzaDati(line)                        
                        try:                            
                            for line_ in dati:
                                out=str(u'\t').join(line_)+u'\n'
                                fout.write(out)
                        except:
                            print "Errore durante la scrittura del file di output"
                            print "line",line
                            print "data",dati
                            
                            return False
        except:
            return             


    def __ElaboraClitico(self, fileinput, fileoutput):
        try:
            os.remove(fileoutput)
        except:
            pass
        
        obj = AnalizzatoreCli()
        try:
            with codecs.open(fileinput, 'r', 'utf-8') as fin:                
                with codecs.open(fileoutput, 'a','utf-8') as fout:
                    for line in fin:
                        line=self.__SeparaColonne(line)
                        if self.__Is2Tag(line, u'VER',u'cli'):
                            dati = obj.AnalizzaDati(line)   
                        else:
                            dati = [line]
                        try:                            
                            for line_ in dati:
                                out = str(u'\t').join(line_)+u'\n'
                                fout.write(out)
                        except:
                            print "Errore durante la scrittura del file di output"
                            print "line",line
                            print "data",dati
                            
                            return False
        except:
            return             




    def __ElaboraDati(self, fileinput, fileoutput):        
       
        filetmp="tempforpurificatore.tmp.txt"
        print "Processo Elabora Apostrofo in corso"
        if self.eliminaApostrofo:
            self.__ElaboraApostrofo(fileinput,filetmp)
        
        print "Processo Elabora Clitico in corso"
        if self.elaboraClitico:
            self.__ElaboraClitico(filetmp,fileoutput)
        
        try:
            os.remove(filetmp)
        except:
            pass
        
        
    def __IsIn(self, line, tag):
        if tag in line[0]:
            return True
        else:
            return False

 
    def __Is2Tag(self, line, tag1, tag2):
        if tag1 in line[1] and tag2 in line[1]:
            return True
        else:
            return False


    def __SeparaColonne(self, line):
        line=line.split('\t')
        line[2]=line[2].replace(u'\n',u'')

        return line
     
                
                
if __name__=='__main__':
    fileinp='input.txt'
    fileout='output_2.txt'
    
    a=Purificatore(fileinp,fileout)
    
    print "done"
        
        