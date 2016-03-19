# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 12:09:26 2016

@author: Patrizio

    questa classe si occupa di sistemare le parole con l'apostrofo
    le separa e cerca di coniugare l'articolo alla forma corretta

"""
import codecs

class AnalizzatoreApostrofo:
    def VERSION(self):
        return "Versione 0.6.b"
    
    def __init__(self):
        pass
    
    
    def __IsIn(self, line, tag):
        if tag in line[0]:
            return True
        else:
            return False
         
    def __IsTag(self, line, tag):
        if tag in line[1]:
            return True
        else:
            return False
            
    def AnalizzaDati(self, line):
        #cerco di correggere eventuali errori di codifica e/o simboli non alphanum
        if self.__IsIn(line, u'``'):            
            return [[u"''", u'PUN', u"''"]] 
        if self.__IsIn(line, u"''"):     
            return [[u"''", u'PUN', u"''"]] 
            
        if self.__IsTag(line,u'NOCAT'):
            if line[0]==u'\xe8':
                return [[u'\xe8', u"VER:pres__mettere_tag_corretta", u"essere"]]
    
#            with codecs.open("NOCAT.txt",'a','utf-8') as f:
#                out=str(u'\t').join(line)+u'\n'
#                f.write(out)
            return [line]
        
        if self.__IsIn(line, u"'") and len(line[0])>2:
            out=list()
            
            sep=line[0].index(u"'")
            pre=line[0][:1+sep]
            post=line[0][sep+1:]
            
            #controllo se l'apostrofo è messo in fondo alla parola, per indicare l'accento
            if len(pre)>=2 and len(post)==0:
                return [line]
            
            pre=[pre,u'ART__',pre]
            post=[post,u'NOUN__',post]
            
            if pre[0]!=u"'":
                out.append(pre)
            if post[0]!=u"'":
                out.append(post)
            return out

        return [line]

