# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 17:36:21 2016

@author: Patrizio
"""
from __future__ import unicode_literals

import sys

from Purificatore import Purificatore

try:        
    if len(sys.argv)==3:
    
        #richiamo le classi che si occupano di elaborare il file
        Purificatore(sys.argv[1], sys.argv[2])

    else:
        print """ATTENZIONE: il file di destinazione verrà sostituito\n     \
        per procedere è necessario specificare i file di input e di output come nell'esempio\n \
        >>>python LemmatizPipeline input.txt output.txt"""
     
except:
    print """ATTENZIONE: il file di destinazione verrà sostituito \n  \
        per procedere è necessario specificare i file di input e di output come nell'esempio\n  \
        >>>python LemmatizPipeline input.txt output.txt"""
        