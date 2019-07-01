class Dictionary():
    def __init__(self):
        self._dictionary = dict()

    def isEmpty(self):
        size = len(self.get_Dictionary())
        return size == 0

    def add_Element(self, newElement):
        self._dictionary.update(newElement)

    def has_Key(self, key):
        if key in self.get_Dictionary():
            return True
        else:
            return False

    def has_Value(self, value):
        if value in self.get_Dictionary().values():
            return True
        else:
            return False

    def get_Value(self, key):
        return self._dictionary.get(key)

    def get_Dictionary(self):
        return self._dictionary

    def print_Dictionary(self):
        dic = self.get_Dictionary()
        for x in dic:
            print "Llave : <%s>\t\t\t\t Valor: <%s>" %(x,dic[x])
