
class SymbolTable:
    
    def __init__(self):
        self.symbol_table = {}

    def insert(self, name, type, value):
        if name not in self.symbol_table:
            self.symbol_table[name] = {"type": type, "value": value}
        else:
            print("{name} is already declared.")

    def search(self, name):
        if name in self.symbol_table:
            return self.symbol_table[name]
        else:
            print("{name} doesn't exist.")
            return None

    def delete(self, name):
        if name in self.symbol_table:
            del self.symbol_table[name]
        else:
            print("{name} doesn't exist.")
    
