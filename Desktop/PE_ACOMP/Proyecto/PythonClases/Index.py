import FileManager
import Persist
import Dic
import Appear

class InvertedIndex():
    def __init__(self):
        self._rf = FileManager.ReadFile()
        self._files = dict() #Agregar a persistencia
        self._words = dict() #Agregar a persistencia
        self._persistFiles = Persist.Persistence("files")
        self._persistWords = Persist.Persistence("words")
        self._persistIndex = Persist.Persistence("index")
        self.index = 0
        self.init_Components()

    def init_Components(self):
        if self._persistIndex.exist_persist() == True:
            a = self._persistIndex.get_Persistence()
            self.set_Index(a.get(1))
        else:
            new = {1 : self.index}
            self._persistIndex.update_Persistence(new)
        if self._persistFiles.exist_persist() == True:
            self.set_Files(self._persistFiles.get_Persistence())
        else:
            new = {}
            self._persistFiles.update_Persistence(new)
        if self._persistWords.exist_persist() == True:
            self.set_Words(self._persistWords.get_Persistence())
        else:
            new = {}
            self._persistWords.update_Persistence(new)

    def index_Files(self, directory ,listFiles):
        for f in listFiles:
            fullPath = directory + "/" + f
            if (fullPath in self.get_Files().values()) == False:
                new = {self.index : fullPath}
                self.get_Files().update(new)
                self.index_Words(self.index, fullPath)
                self.index += 1
        self._persistFiles.update_Persistence(self.get_Files())
        newIndex = {1 : self.index}
        self._persistIndex.update_Persistence(newIndex)

    def index_Words(self, docID, path):
        rawData = self._rf.read_File(path)
        self._rf.delete_StopWords(rawData)
        data = self._rf.get_dataWords() #Pila con todas las palabras que debo evaluar
        while data.isEmpty() == False:
            aux = data.pop()
            if (aux in self.get_Words().keys()) == True:
                appearanceList = self.get_Words().get(aux)
                isInArray = False
                for x in appearanceList:
                    if x.get_DocID() == docID:
                        x.add_Casualty()
                        isInArray = True
                        break
                if isInArray == False:
                    ap1 = Appear.Appearance(docID, 1)
                    appearanceList.append(ap1)
            else:
                linkedList = []
                ap2 = Appear.Appearance(docID, 1)
                linkedList.append(ap2)
                new = {aux : linkedList}
                self.get_Words().update(new)
        self._persistWords.update_Persistence(self.get_Words())

    def get_Files(self):
        return self._files

    def set_Files(self, data):
        self._files = data

    def get_Words(self):
        return self._words

    def set_Words(self, data):
        self._words = data

    def set_Index(self, newIndex):
        self.index = newIndex
