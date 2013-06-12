class element:
    key = int()
    value = str()
    
    def __init__(self, key, value):
        self.key = key
        self.value = value

class hashTable:
    __buckets = list()
    __bucketsCount = int()      
            
    def __init__(self, bucketsCount):
        self.__bucketsCount = bucketsCount
        for i in range(bucketsCount):
            self.__buckets.append(list())

    def add(self,key,value):
        k = key % self.__bucketsCount
        b = self.__buckets[k]
        e = element(key, value)
        if self.findByKey(key):
            self.delete(key)
        b.append(e)

    def delete(self, key):
        k = key % self.__bucketsCount
        b = self.__buckets[k]
        for i in b:
            if i.key == key:
                b.remove(i)
                return "OK. removal done"
        return "removal fails"

    def findByKey(self, key):
        s = Hash(key)
        k = key % self.__bucketsCount
        b = self.__buckets[k]
        for i in b:
            if Hash(i.key) == s:
                return "OK. item is found"
        return "item is not found"

    def findByValue(self, value):
        for i in self.__buckets:
            for j in i:
                if j.value == value:
                    return "OK. item is found"
        return "item is not found"

    def get(self, key):
        s = Hash(key)
        k = key % self.__bucketsCount
        b = self.__buckets[k]
        for i in b:
            if Hash(i.key) == s:
                return i.value 
        return None

def Hash(value):
        S=0
        for i in str(value):
            S+=ord(i)
        return S


tab = hashTable(3)
