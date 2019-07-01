import os
import re
import Persist
import Dic

def recover():
    a = Persist.Persistence("files")
    data = a.get_Persistence()
    print_Dictionary(data)

def print_Dictionary(Dictionary):
    for x in Dictionary:
        print "Llave : <%s>\t\t\t\t Valor: <%s>" %(x,Dictionary[x])

a = recover()
