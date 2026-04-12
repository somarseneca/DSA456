class ChainingTable:

    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
        self.cap = capacity
        self.table = [None for _ in range(self.cap)]
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.cap

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = [None] * 1
            self.table[index][0] = self.Record(key, value)
            self.size += 1
        else:
            chain = self.table[index]

            i = 0
            while i < len(chain):
                if chain[i] is not None and chain[i].key == key:
                    return False
                i += 1

            new_chain = [None] * (len(chain) + 1)

            i = 0
            while i < len(chain):
                new_chain[i] = chain[i]
                i += 1

            new_chain[len(chain)] = self.Record(key, value)
            self.table[index] = new_chain
            self.size += 1

        if self.size / self.cap > 1.0:
            self._resize()

        return True

    def modify(self, key, value):
        index = self._hash(key)

        chain = self.table[index]
        if chain is None:
            return False

        i = 0
        while i < len(chain):
            if chain[i] is not None and chain[i].key == key:
                chain[i].value = value
                return True
            i += 1

        return False

    def remove(self, key):
        index = self._hash(key)

        chain = self.table[index]
        if chain is None:
            return False

        i = 0
        while i < len(chain):
            if chain[i] is not None and chain[i].key == key:

                j = i
                while j < len(chain) - 1:
                    chain[j] = chain[j + 1]
                    j += 1

                chain[len(chain) - 1] = None
                self.size -= 1
                return True

            i += 1

        return False

    def search(self, key):
        index = self._hash(key)

        chain = self.table[index]
        if chain is None:
            return None

        i = 0
        while i < len(chain):
            if chain[i] is not None and chain[i].key == key:
                return chain[i].value
            i += 1

        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.size

    def _resize(self):
        old_table = self.table

        self.cap *= 2
        self.table = [None for _ in range(self.cap)]
        self.size = 0

        i = 0
        while i < len(old_table):
            chain = old_table[i]

            if chain is not None:
                j = 0
                while j < len(chain):
                    if chain[j] is not None:
                        self.insert(chain[j].key, chain[j].value)
                    j += 1

            i += 1



# TEST CASES

if __name__ == "__main__":
    table = ChainingTable()

    print(table.insert("a", 1))  # True
    print(table.insert("b", 2))  # True
    print(table.insert("a", 3))  # False

    print(table.search("a"))  # 1
    print(table.modify("a", 100))  # True
    print(table.search("a"))  # 100

    print(table.remove("b"))  # True
    print(table.search("b"))  # None

    print(len(table))  # 1
    print(table.capacity())  # 32+

    # Resize test
    t2 = ChainingTable(2)
    i = 0
    while i < 5:
        t2.insert("key" + str(i), i)
        i += 1

    print(len(t2))        # 5
    print(t2.capacity()) # should increase