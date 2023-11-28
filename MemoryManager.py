
from collections import defaultdict
from PiinkkLoader import piinkkLoader

class MemoryManager():
    # Constants
    SIZE_PER_MEMORY = 1000
    GLOBAL_INT_I = 5000
    GLOBAL_FLOAT_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 1
    GLOBAL_BOOL_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 2
    LOCAL_INT_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 3
    LOCAL_FLOAT_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 4
    LOCAL_BOOL_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 5
    TEM_INT_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 6
    TEM_FLOAT_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 7
    TEM_BOOL_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 8
    CTE_INT_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 9
    CTE_FLOAT_I = GLOBAL_INT_I + SIZE_PER_MEMORY * 10
    MEMORY_SIZE = CTE_FLOAT_I - GLOBAL_INT_I + SIZE_PER_MEMORY

    def __init__(self):
        self.count = 0
        self.globals = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.locals = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.temps = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.ctes = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.memory = [None] * (self.CTE_FLOAT_I + self.MEMORY_SIZE)
        self.setAdresses()
    
    def setAdresses(self):
        # Set initial and final addresses for each data type in each memory scope
        self.globals['int']['iniAdd'] = self.GLOBAL_INT_I
        self.globals['int']['finAdd'] = self.GLOBAL_FLOAT_I - 1
        self.globals['float']['iniAdd'] = self.GLOBAL_FLOAT_I
        self.globals['float']['finAdd'] = self.GLOBAL_BOOL_I - 1
        self.globals['bool']['iniAdd'] = self.GLOBAL_BOOL_I
        self.globals['bool']['finAdd'] = self.LOCAL_INT_I - 1
        self.locals['int']['iniAdd'] = self.LOCAL_INT_I
        self.locals['int']['finAdd'] = self.LOCAL_FLOAT_I - 1
        self.locals['float']['iniAdd'] = self.LOCAL_FLOAT_I
        self.locals['float']['finAdd'] = self.LOCAL_BOOL_I - 1
        self.locals['bool']['iniAdd'] = self.LOCAL_BOOL_I
        self.locals['bool']['finAdd'] = self.TEM_INT_I - 1
        self.temps['int']['iniAdd'] = self.TEM_INT_I
        self.temps['int']['finAdd'] = self.TEM_FLOAT_I - 1
        self.temps['float']['iniAdd'] = self.TEM_FLOAT_I
        self.temps['float']['finAdd'] = self.TEM_BOOL_I - 1
        self.temps['bool']['iniAdd'] = self.TEM_BOOL_I
        self.temps['bool']['finAdd'] = self.CTE_INT_I - 1
        self.ctes['int']['iniAdd'] = self.CTE_INT_I
        self.ctes['int']['finAdd'] = self.CTE_FLOAT_I - 1
        self.ctes['float']['iniAdd'] = self.CTE_FLOAT_I
        self.ctes['float']['finAdd'] = self.CTE_FLOAT_I + self.MEMORY_SIZE - 1
        
    def getNewAddress(self, memory_scope, data_type):
        # Determine the memory scope dictionary
        if memory_scope == 'global':
            scope = self.globals
        elif memory_scope == 'temp':
            scope = self.temps
        elif memory_scope == 'ctes':
            scope = self.ctes
        else:
            scope = self.locals

        # Calculate the new address
        newAddress = scope[data_type]['iniAdd'] + scope[data_type]['count']

        # Check for memory overflow
        if newAddress > scope[data_type]['finAdd']:
            raise Exception('Memory overflow')

        # Increment the count for the data type in the memory scope
        scope[data_type]['count'] += 1

        # Return the new address
        return newAddress

    def getValue(self, address):
        return self.memory[address]
    
    def setValue(self, address, value):
        self.memory[address] = value
        # self.memory[0] = 'hola'

    def getType(self, address):
        if address >= self.GLOBAL_INT_I and address < self.GLOBAL_FLOAT_I:
            return 'int'
        elif address >= self.GLOBAL_FLOAT_I and address < self.GLOBAL_BOOL_I:
            return 'float'
        elif address >= self.GLOBAL_BOOL_I and address < self.LOCALS_INT_I:
            return 'bool'
        elif address >= self.LOCALS_INT_I and address < self.LOCALS_FLOAT_I:
            return 'int'
        elif address >= self.LOCALS_FLOAT_I and address < self.LOCALS_BOOL_I:
            return 'float'
        elif address >= self.LOCALS_BOOL_I and address < self.TEM_INT_I:
            return 'bool'
        elif address >= self.TEM_INT_I and address < self.TEM_FLOAT_I:
            return 'int'
        elif address >= self.TEM_FLOAT_I and address < self.TEM_BOOL_I:
            return 'float'
        elif address >= self.TEM_BOOL_I and address < self.CTE_INT_I:
            return 'bool'
        elif address >= self.CTE_INT_I and address < self.CTE_FLOAT_I:
            return 'int'
        elif address >= self.CTE_FLOAT_I and address < self.CTE_FLOAT_I + self.MEMORY_SIZE - 1:
            return 'float'
        else:
            return None

    def resetCountLocal(self):
        # Reset the count for each data type in the local memory scope
        self.locals['int']['count'] = 0
        self.locals['float']['count'] = 0
        self.locals['bool']['count'] = 0
    
    def resetCountTemp(self):
        # Reset the count for each data type in the temporary memory scope
        self.temps['int']['count'] = 0
        self.temps['float']['count'] = 0
        self.temps['bool']['count'] = 0



memoryManager = MemoryManager()
#
#This code defines a `MemoryManage` class that manages memory allocation for different memory scopes and data types.
# The class uses dictionaries to store the count, initial address, and final address for each data type in each memory scope.
# The `getNewAddress` method calculates the new address for a given memory scope and data type, checks for memory overflow,
# increments the count, and returns the new address. The `resetCountLocal` and `resetCountTemp` methods reset the count
# for each data type in the local and temporary memory scopes, respectively..</s>