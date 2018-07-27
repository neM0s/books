import biblioteki.kalkulator

from biblioteki.kalkulator import suma # trafia do biezacej przestrzeni nazw, srednio zle - utrudnia analize
#from kalkulator import * # calkiem zle - przeslania nazwy, uniemozliwia przesledzenie pochodzenia

k2 = __import__("kalkulator")
print(k2.suma(10,15))

print(suma(1,23))
print(biblioteki.kalkulator.suma(1,23))

import sys

print(sys.path)