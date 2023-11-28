
from ast import operator
from semanticCube import *
from collections import defaultdict

class PiinkkLoader():
    def __init__(self):
        self.operator_stack = []
        self.operator_stack_dir = []
        self.type_stack = []
        self.operand_stack = []
        self.jump_stack = []
        self.symbol_table = defaultdict(lambda:{'variables':{}})
        self.current_scope = 'global'
        self.pendientes = []
        self.temporal = 1
        self.quadruples = []
        self.param_count = 0
        self.current_fun = ''

    def set_current_scope(self, scope_name):
        self.current_scope = scope_name

    def variableCheck(self, name):
        if name in self.symbol_table['global']['variables']:
            self.stopExecution(f'Variable \'{name}\' is already declared in global scope.')
        
        if self.current_scope != 'global':
            if name in self.symbol_table[self.current_scope]['variables']:
                self.stopExecution(f'Variable \'{name}\' is already declared in current scope.')
        
    def functionCheck(self, name):
        if name in self.symbol_table:
            self.stopExecution(f'Function \'{name}\' is already declared.')

    def functionCallCheck(self, name):
        if name not in self.symbol_table:
            self.stopExecution(f'Function \'{name}\' is not declared.')

    def getType(self, name):
        if name in self.symbol_table['global']['variables']:
            return self.symbol_table['global']['variables'][name]['type']
        elif name in self.symbol_table[self.current_scope]['variables']:
            return self.symbol_table[self.current_scope]['variables'][name]['type']
        else:
            self.stopExecution(f'Variable \'{name}\' is not declared.')

    def getTemporal(self):
        return self.temporal
    
    def addQuadruple(self, quadruple):
        self.quadruples.append(quadruple)
        print(f'\t\t    {len(self.quadruples)}')

    def clearStacks(self):
        self.operator_stack = []
        self.type_stack = []
        self.operand_stack = []

    def isNumber(self, text):
        try:
            int_value = int(text)
            return 'int'
        except ValueError:
            try:
                float_value = float(text)
                return 'float'
            except:
                return False
    
    def set_param_count(self, count):
        self.param_count = count

    def getAddress(self, name):
        if name in self.symbol_table['global']['variables']:
            return self.symbol_table['global']['variables'][name]['address']
        elif name in self.symbol_table[self.current_scope]['variables']:
            return self.symbol_table[self.current_scope]['variables'][name]['address']
        elif name in self.symbol_table['temp']['variables']:
            return self.symbol_table['temp']['variables'][name]['address']
        elif name in self.symbol_table['cte']['variables']:
            return self.symbol_table['cte']['variables'][name]['address']
        else:
            return None
            # self.stopExecution(f'Variable \'{name}\' does not have an assignated address.')

    def stopExecution(self, errorType):
        print(errorType)
        exit()

piinkkLoader = PiinkkLoader()


# {'global': {'variables': {'i': {'type': 'int'}}}
# 'function1': {'variables': {'x': {'type': 'int'}}, 'type': 'void' }
# 'function2': {'variables': {'y': {'type': 'int'}}, 'type': 'void' }
# }

#
#In this code, we have a class called `PiinkkLoader` that is responsible for loading and managing the semantic information of a program. It has several methods for checking and managing the symbol table, handling errors, and generating quadruples.
#
#The `variableCheck` method checks if a variable with the given name is already declared in the global or current scope. If it is, an error message is printed and the program execution is stopped.
#
#The `functionCheck` method checks if a function with the given name is already declared. If it is, an error message is printed and the program execution is stopped.
#
#The `functionCallCheck` method checks if a function with the given name is declared. If it is not, an error message is printed and the program execution is stopped.
#
#The `getType` method returns the type of a variable with the given name. If the variable is not declared, an error message is printed and the program execution is stopped.
#
#The `getTemporal` method returns the current value of the `temporal` attribute, which is used to generate unique temporary variable names.
#
#The `addQuadruple` method adds a quadruple to the `quadruples` list.
#
#The `clearStacks` method clears the `operator_stack`, `type_stack`, and `operand_stack` attributes.
#
#The `isNumber` method checks if a given text can be converted to an integer or a float. It returns the corresponding type if the conversion is successful, and `False` otherwise.
#
#Finally, the `stopExecution` method prints an error message and stops the program execution.