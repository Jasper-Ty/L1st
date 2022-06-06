"""Module which provides a 1-indexed list class named l1st"""

class l1st(list):

    """Python list wrapper that begins indexing at 1"""
    
    def __init__(self, *args):
        super().__init__(*args)

    def __getitem__(self, key):
        return super().__getitem__(key-1)
    
    def __setitem__(self, key, val):
        super().__setitem__(key-1, val)

    def index(self, value):
        return super().index(value)+1
    
    def insert(self, index, item):
        super().insert(index-1, item)

    def pop(self, *args):
        idx = args[0]-1 if args else -1
        super().pop(idx)
    