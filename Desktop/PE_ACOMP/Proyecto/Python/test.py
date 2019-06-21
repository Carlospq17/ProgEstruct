class Appearance:
    """
    Represents the appearance of a term in a given document, along with the
    frequency of appearances in the same one.
    """
    def __init__(self, docID, frequency):
        self.docID = docID
        self.frequency = frequency

    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)

    def add_Casualty(self):
        self.frequency += 1

    def get_DocID(self):
        return self.get_DocID

    def get_Frequency(self):
        return self.frequency

diccionario = {}
ap1 = Appearance(1, 0)
ap2 = Appearance(2, 0)
ap3 = Appearance(3, 0)
lista1 = []
lista2 = []
lista1.append(ap1)
lista2.append(ap2)
newDic = {"word" : lista1, "word2" : lista2}

diccionario.update(newDic)
listado = diccionario.get("word")
listado[0].add_Casualty()
listado[0].add_Casualty()
listado[0].add_Casualty()
listado[0].add_Casualty()
listado2 = diccionario.get("word2")
listado2.append(ap3)
listado2[1].add_Casualty()
listado2[1].add_Casualty()
listado2[0].add_Casualty()
print diccionario

#-> /Users/carlospool/Desktop/PE_ACOMP/Proyecto/Python
#-> python test.py
