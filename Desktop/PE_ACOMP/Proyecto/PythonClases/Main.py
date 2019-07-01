import re
import os
import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import Sort
import Index
import emptyDictError
import notKeyError
import notDirectoryError

class MainWindow(Frame):
    def __init__(self):
        self._invIndex = Index.InvertedIndex()
        Frame.__init__(self)
        self.pack( fill = BOTH)
        self.master.title("Explorador de archivos (.txt)")
        self.master.geometry("325x100")

        self.frame1 = Frame(self)
        self.frame1.pack(pady = 5)
        self.frame2 = Frame(self)
        self.frame2.pack(pady = 5)

        self.infoDirectory = Label(self.frame1, text = "Ingrese un directorio...")
        self.infoDirectory.pack(side = LEFT, padx = 5)
        self.infoWord = Label(self.frame2, text = "Ingrese una palabra")
        self.infoWord.pack(side = LEFT, padx = 5)

        self.inputDirectory = Entry(self.frame1, name = "inputDirectory")
        self.inputDirectory.bind("<Return>", self.add_Directory)#aqui va un add_Directory
        self.inputDirectory.pack(side = LEFT, padx = 5)

        self.inputWord = Entry(self.frame2, name = "inputWord")
        self.inputWord.bind("<Return>", self.search_Word)#aqui va un serchword
        self.inputWord.pack(side = LEFT, padx = 5)

    def add_Directory (self, event):
        try:
            content = event.widget.get();
            directory = str(content)
            if os.path.isdir(directory) == True:
                showinfo("Message", "Is Directory")
                onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and (re.search(".txt", f) != None or re.search(".TXT", f) != None) ]
                self.get_invertedIndex().index_Files(directory,onlyfiles)#Esta funcion indexa los archivos y sus palabras
            else:
                raise notDirectoryError.notDirectory("La cadena: <<%s>> NO es un directorio" %directory)
        except Exception as e:
            print (e.message)
            showinfo("Message", e.message)

    def search_Word(self, event):
        try:
            content = event.widget.get()
            test = str(content)
            available = len( self.get_invertedIndex().get_Words() )
            if available != 0:
                if (test in self.get_invertedIndex().get_Words()) == True :
                    sortTool = Sort.Ordenamiento()
                    toSort = self.get_invertedIndex().get_Words().get(test)
                    size = len(toSort)
                    sortTool.QuickSort(toSort, 0, size-1)
                    self.show_Recomendation(toSort)
                else:
                    raise notKeyError.notKey("La palabra <<%s>> NO se encuentra en los archivos"%test)
            else:
                raise emptyDictError.emptyDictionary("El diccionario se encuentra vacio")
        except Exception as e:
            print (e.message)
            showinfo("Message", e.message)

    def show_Recomendation(self, sortedList):
        results = tk.Tk()
        results.title("Resultados")
        texto = tk.Text(results, height = 10, width = 100)
        texto.insert(tk.INSERT, "Archivo \t\t\t\t\t\t\t\t\t Coincidencias\n")
        for x in sortedList:
            texto.insert(tk.INSERT, "%s \t\t\t   |%s\n" %(self.get_invertedIndex().get_Files().get(x.get_DocID()), x.get_Frequency() ))
        texto.pack()

    def get_invertedIndex(self):
        return self._invIndex

    def showContents(self, event): #Deprecated
        theName = event.widget.winfo_name()
        theContents = event.widget.get()
        showinfo("Message", theName + ": " + theContents)

def main():
    MainWindow().mainloop()
if __name__ == "__main__":
    main()
