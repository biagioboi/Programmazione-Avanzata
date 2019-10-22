class MyDictionary:
    class MyPair:
        def __init__(self, k, v):
            self.key = k
            self.value = v

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value

        def setKey(self, k):
            self.key = k

        def setValue(self, v):
            self.value = v

    def __init__(self):
        self._L = []

    def __setitem__(self, key, value):
        for p in self._L:
            if p.getKey() == key:
                p.setValue(value)
                return
        self._L.append(MyDictionary(key, value))
        return

    def __str__(self):
        pass
    def __delitem__(self, key):
        pass
    def __getitem__(self, item):
        pass
    def __eq__(self, other):
        pass
