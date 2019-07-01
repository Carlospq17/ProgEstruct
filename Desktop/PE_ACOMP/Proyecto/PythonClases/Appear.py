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
