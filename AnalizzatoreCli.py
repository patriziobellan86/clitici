# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:04:33 2016

@author: Patrizio

resource http://images.treccani.it/enc/media/share/images/orig//system/galleries/ENCICLOPEDIA_DELL_ITALIANO/I_VOLUME/TABELLE/015_Clitici_1.jpg

        
"""


from __future__ import unicode_literals


class AnalizzatoreCli:

    def VERSION(self):
        return "Versione 0.6.b"
        
        
    def __init__(self):
        self.elencoClitici=[u'si',u'gli',u'mi',u'ne',u'li',u'lo',u'le',u'la',u'ci',u'vi',u'ti']
        self.desinenzeInfinito=[u'are',u'ere',u'ire']
        
       
    def __IsIn(self, line, tag):
        if tag in line[1]:
            return True
        else:
            return False

        
    def AnalizzaDati(self, line):
        out=list()
        for desinenzacli in self.elencoClitici:
            if line[0].endswith(desinenzacli):
                
                _=line[2]
                _=_.strip()
                line[0]=_

                out.append(line)
                out.append([desinenzacli,u'CLI',desinenzacli])

                return out
                
        #se sono giunto qui vuol dire che NON era un verbo clitico 
        return [line]