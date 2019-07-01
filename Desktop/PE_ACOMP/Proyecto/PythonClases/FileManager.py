import re
import stack
import Persist
import Dic

class ReadFile(object):
    def __init__ (self):
        self._dataWords = stack.Stack() #Devuelve una pila con todas las palabras que no son stopwords
        self._persistStopWords = Persist.Persistence("stopWords")
        self._StopWords = dict()
        self.init_Components()

    def init_Components(self):
        if self._persistStopWords.exist_persist() == True:
            self.set_StopWords(self._persistStopWords.get_Persistence())
        else:
            sw = self.read_File("/Users/carlospool/Desktop/PE_ACOMP/Proyecto/StopWords/Stop_WordsEN.txt")
            for x in sw:
                x = re.sub("\n", "", x)
                new = {x : 1}
                self.get_StopWords().update(new)
            self._persistStopWords.update_Persistence(self.get_StopWords())

    def read_File (self, dir):
        data = open(dir, "r")
        lines = data.readlines()
        data.close()
        return lines

    def delete_StopWords (self, data):
        #dataStopWords
        self._dataWords = stack.Stack()
        i = 0
        count1 = len(data)
        while i < count1:
            j = 0
            clean_Text = re.sub(r'[^\w\s]',"",data[i])
            aux = clean_Text.split()
            count2 = len(aux)
            while j < count2:
                if (aux[j] in self.get_StopWords().keys()) == True:
                    aux[j] = ""
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

    def get_dataWords(self):
        return self._dataWords

    def get_StopWords(self):
        return self._StopWords

    def set_StopWords(self, new):
        self._StopWords.update(new)
