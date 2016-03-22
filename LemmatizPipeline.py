# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 17:36:21 2016

@author: Patrizio
"""
from __future__ import unicode_literals

import sys

from Purificatore import Purificatore

mex = """
        ATTENZIONE: il file di destinazione verrà sostituito\n     \
        per procedere è necessario specificare i file di input e di output come nell'esempio\n \
        >>>python LemmatizPipeline input.txt output.txt [-c -a]
        parametri:
           -c ->  non elaborare il clitico
           -a ->  non elaborare l'apostrofo
        """
try:        
    if len(sys.argv) >= 3:
        if len (sys.argv) == 4 and sys.argv[-1] == '-c':
            Purificatore(sys.argv[1], sys.argv[2], False, True)
        elif len (sys.argv) == 4 and sys.argv[-1] == '-a':
            Purificatore(sys.argv[1], sys.argv[2], True, False)
        elif len (sys.argv) == 5 and sys.argv[-2] == '-c' and sys.argv[-1] == '-a':
            print "Attenzione questa opzione non ha senso perchè non vengono effettuati calcoli!"
            print
            print mex
            
    else:
        print mex
except:
    print mex
        