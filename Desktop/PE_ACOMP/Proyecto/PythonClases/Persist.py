import os
import pickle
import Dic

class Persistence():
    def __init__ (self, name):
        self._name = name + ".pickle"

    def update_Persistence(self, data):
        #nameFile = nameFile + ".pickle"
        with open(self._name, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def get_Persistence(self):
        #nameFile = nameFile + ".pickle"
        with open(self._name, 'rb') as handle:
            output = pickle.load(handle)
        return output

    def exist_persist(self):
        return os.path.exists(os.path.realpath(self._name))
