import re
import os

class Ordenamiento:
    def partition(self,array, left, right):
        i = (left-1)
        pivot = array[right]

        for j in range(left, right):
            if array[j] <= pivot:
                i = i + 1
                array[i],array[j] = array[j], array[i]

        array[i + 1], array[right] = array[right], array[i + 1]
        return (i + 1)

    def QuickSort (self,array, left, right):
        if left < right:
            partitionIndex = self.partition(array, left, right)
            self.QuickSort(array, left, partitionIndex - 1)
            self.QuickSort(array, partitionIndex + 1, right)

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class ReadFile(object):
    def __init__ (self):
        self._dataFinal = [] #Devuelve el parrafo completo sin stopWords
        self._dataWords = Stack() #Devuelve una pila con todas las palabras que no son stopwords

    def read_File (self, dir):
        data = open(dir, "r")
        lines = data.readlines()
        data.close()
        return lines

    def delete_StopWords (self, data, dataStopWords):
        self._dataFinal = []
        self._dataWords = Stack()
        i = 0
        count1 = len(data)
        while i < count1:
            j = 0
            clean_Text = re.sub(r'[^\w\s]',"",data[i])
            aux = clean_Text.split()
            count2 = len(aux)
            while j < count2:
                k = 0
                count3 = len(dataStopWords)
                while k < count3:
                    temp1 = str(aux[j].split())
                    temp2 = str(dataStopWords[k].split())
                    if temp2 == temp1:
                        aux[j] = ""
                    k += 1
                j += 1
            i += 1
            l = 0
            count4 = len(aux)
            cadena = ""
            while l < count4:
                temp3 = str(aux[l])
                if temp3 != "":
                    cadena = cadena + aux[l] +  " "
                    self._dataWords.push(aux[l])
                l += 1
            self._dataFinal.append(cadena)

    def print_Words (self): #Deprecated
        print "===================================================="
        while self._dataWords.isEmpty() == False:
            print self._dataWords.pop()
        print "===================================================="

    def print_Text(self):
        size = len(self._dataFinal)
        i = 0
        print "===================================================="
        while i < size :
            print "->",self._dataFinal[i]
            i += 1
        print "===================================================="

    def get_dataFinal(self):
        return self._dataFinal

    def get_dataWords(self):
        return self._dataWords

class Dictionary():
    def __init__(self):
        self._dictionary = dict()

    def add_Element(self, newElement):
        self._dictionary.update(newElement)

    def has_Key(self, key):
        if key in self.get_Dictionary():
            return True
        else:
            return False

    def get_Value(self, key):
        return self._dictionary.get(key)

    def get_Dictionary(self):
        return self._dictionary

    def clear_Directory(self):
        self._dictionary

    def print_Dictionary(self):
        dic = self.get_Dictionary()
        for x in dic:
            print "Llave : %s\t\t\t\t\t\t\t Valor: %s" %(x,dic[x])

class Appearance():
    def __init__(self, docID, frequency):
        self._docID = docID
        self._frequency = frequency

    def __repr__(self):
        return "(ID:%d , F:%d)"%(self.get_DocID(), self.get_Frequency())

    def add_Casualty(self):
        self._frequency += 1

    def get_DocID(self):
        return self._docID

    def get_Frequency(self):
        return self._frequency

class InvertedIndex():
    def __init__(self):
        self._rf = ReadFile()
        self.stopWords = self._rf.read_File("/Users/carlospool/Desktop/PE_ACOMP/Proyecto/StopWords/Stop_WordsEN.txt")
        self._files = Dictionary()
        self._words = Dictionary()
        self.index = 0

    def index_Files(self, directory ,listFiles):
        for f in listFiles:
            fullPath = directory + "/"
            isTxt = re.search(".txt", f)
            if isTxt != None:
                fullPath = fullPath + f
                new = {self.index : fullPath}
                self.get_Files().add_Element(new)
                self.index_Words(self.index, fullPath)
                self.index += 1
        print "========================================================================"
        print "Diccionario de archivos \n", self.get_Files().print_Dictionary()
        print "========================================================================"
        print "Diccionario de palabras \n", self.get_Words().print_Dictionary()
        print "========================================================================"

    def index_Words(self, docID, path):
        rawData = self._rf.read_File(self.get_Files().get_Value(docID))
        self._rf.delete_StopWords(rawData, self.stopWords)
        data = self._rf._dataWords #Pila con todas las palabras que debo evaluar
        while data.isEmpty() == False:
            aux = data.pop()
            if self.get_Words().has_Key(aux):
                appearanceList = self.get_Words().get_Value(aux)
                isInArray = False
                for x in appearanceList:
                    if x.get_DocID() == docID:
                        x.add_Casualty()
                        isInArray = True
                        break
                if isInArray == False:
                    ap1 = Appearance(docID, 1)
                    appearanceList.append(ap1)
            else:
                linkedList = []
                ap2 = Appearance(docID, 1) # va el docID y su frecuencia de inicio que es 1
                linkedList.append(ap2)
                new = {aux : linkedList}
                self.get_Words().add_Element(new)

    def get_Files(self):
        return self._files

    def get_Words(self):
        return self._words

class Main(ReadFile):
    def trigger (self):
        invIndex = InvertedIndex()

        print "Para este programa solo se aceptaran archivos de texto en ingles(.txt)"
        while True:
            directory = raw_input("Ingrese un directorio...\n") #Directorio que sera evaluado y procesado por el programa
            if os.path.isdir(directory) == True:
                onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))] #Metodo para determinar archivos
                invIndex.index_Files(directory,onlyfiles)#Esta funcion indexa los archivos y sus palabras
            else:
                print "La cadena ingresada No es un Directorio"
            answer = int(raw_input("Es el unico directorio que desea agregar? 1 = Si\n"))
            if answer == 1:
                break

inicio = Main()
inicio.trigger()

#-> alias proy /Users/carlospool/Desktop/PE_ACOMP/Proyecto/Python
#-> alias runproy /Users/carlospool/Desktop/PE_ACOMP/Proyecto/exampleTxt
#-> python proyect.py
