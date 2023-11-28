
from collections import defaultdict

class MemoryManage:
    # Constants
    GLOBAL_INT_I = 5000
    GLOBAL_INT_F = 5999
    GLOBAL_FLOAT_I = 6000
    GLOBAL_FLOAT_F = 6999
    GLOBAL_BOOL_I = 7000
    GLOBAL_BOOL_F = 7999
    LOCAL_INT_I = 8000
    LOCAL_INT_F = 8999
    LOCAL_FLOAT_I = 9000
    LOCAL_FLOAT_F = 9999
    LOCAL_BOOL_I = 10000
    LOCAL_BOOL_F = 10999
    TEM_INT_I = 11000
    TEM_INT_F = 11999
    TEM_FLOAT_I = 12000
    TEM_FLOAT_F = 12999
    TEM_BOOL_I = 13000
    TEM_BOOL_F = 13999
    CTE_INT_I = 14000
    CTE_INT_F = 14999
    CTE_FLOAT_I = 15000
    CTE_FLOAT_F = 15999

    def __init__(self):
        self.count = 0
        self.globals = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.locals = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.temps = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.ctes = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.setValues()
    
    def setValues(self):
        # Set initial and final addresses for each data type in each memory scope
        self.globals['int']['iniAdd'] = self.GLOBAL_INT_I
        self.globals['int']['finAdd'] = self.GLOBAL_INT_F
        self.globals['float']['iniAdd'] = self.GLOBAL_FLOAT_I
        self.globals['float']['finAdd'] = self.GLOBAL_FLOAT_F
        self.globals['bool']['iniAdd'] = self.GLOBAL_BOOL_I
        self.globals['bool']['finAdd'] = self.GLOBAL_BOOL_F
        self.locals['int']['iniAdd'] = self.LOCAL_INT_I
        self.locals['int']['finAdd'] = self.LOCAL_INT_F
        self.locals['float']['iniAdd'] = self.LOCAL_FLOAT_I
        self.locals['float']['finAdd'] = self.LOCAL_FLOAT_F
        self.locals['bool']['iniAdd'] = self.LOCAL_BOOL_I
        self.locals['bool']['finAdd'] = self.LOCAL_BOOL_F
        self.temps['int']['iniAdd'] = self.TEM_INT_I
        self.temps['int']['finAdd'] = self.TEM_INT_F
        self.temps['float']['iniAdd'] = self.TEM_FLOAT_I
        self.temps['float']['finAdd'] = self.TEM_FLOAT_F
        self.temps['bool']['iniAdd'] = self.TEM_BOOL_I
        self.temps['bool']['finAdd'] = self.TEM_BOOL_F
        self.ctes['int']['iniAdd'] = self.CTE_INT_I
        self.ctes['int']['finAdd'] = self.CTE_INT_F
        self.ctes['float']['iniAdd'] = self.CTE_FLOAT_I
        self.ctes['float']['finAdd'] = self.CTE_FLOAT_F
        
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



memoryManage = MemoryManage()
#
#This code defines a `MemoryManage` class that manages memory allocation for different memory scopes and data types.
# The class uses dictionaries to store the count, initial address, and final address for each data type in each memory scope.
# The `getNewAddress` method calculates the new address for a given memory scope and data type, checks for memory overflow,
# increments the count, and returns the new address. The `resetCountLocal` and `resetCountTemp` methods reset the count
# for each data type in the local and temporary memory scopes, respectively..</s>