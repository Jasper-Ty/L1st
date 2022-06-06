"""Module which provides a 1-indexed list class named l1st"""

class l1st:

    """Python list wrapper that begins indexing at 1"""

    def __init__(self, *args): # args[0] should be an iterable
        self._list = list(args[0]) if args else list()
        """L1st instance internal list"""
    
    def __getitem__(self, key):
        return self._list[key-1]
    
    def __setitem__(self, key, val):
        self._list[key-1] = val
    
    def __len__(self):
        return len(self._list)

    def __iter__(self):
        return iter(self._list)
    
    def __contains__(self, item):
        return item in self._list

    def __repr__(self):
        return repr(self._list)
    
    def __str__(self):
        return str(self._list)

    def append(self, item):
        self._list.append(item)
    
    def clear(self):
        self._list.clear()
    
    def copy(self):
        return self._list.copy()
    
    def count(self, item):
        return self._list.count(item)

    def extend(self, iter):
        self._list.extend(iter)
    
    def index(self, value):
        return self._list.index(value)+1
    
    def insert(self, index, item):
        self._list.insert(index-1, item)
    
    def pop(self, *args):
        idx = args[0] if args else -1
        self._list.pop(idx)
    
    def remove(self, item):
        self._list.remove(item)
    
    def reverse(self):
        self._list.reverse()
    
    def sort(self, **kwargs):
        self._list.sort(kwargs)
