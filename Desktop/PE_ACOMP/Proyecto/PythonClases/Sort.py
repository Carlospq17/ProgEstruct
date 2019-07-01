class Ordenamiento:
    def partition(self,array, left, right):
        i = (left-1)
        pivot = array[right].get_Frequency()

        for j in range(left, right):
            if array[j].get_Frequency() >= pivot:
                i = i + 1
                array[i],array[j] = array[j], array[i]

        array[i + 1], array[right] = array[right], array[i + 1]
        return (i + 1)

    def QuickSort (self,array, left, right):
        if left < right:
            partitionIndex = self.partition(array, left, right)
            self.QuickSort(array, left, partitionIndex - 1)
            self.QuickSort(array, partitionIndex + 1, right)

    def Burbuja(self, array): #Deprecated
        for numPasada in range(len(array)-1,0,-1):
            for i in range(numPasada):
                if array[i].get_Frequency() < array[i+1].get_Frequency():
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
