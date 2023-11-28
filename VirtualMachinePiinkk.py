
from MemoryManager import memoryManager
from PiinkkLoader import piinkkLoader

class PiinkkVM():
    def __init__(self, quadruples):
        self.symbol_table = piinkkLoader.symbol_table
        self.quadruples = quadruples
        self.manager = memoryManager
        self.memory = memoryManager.memory
        self.current_function = ''
        self.stack = []   # Stack for managing function calls and expressions
        self.solving = 0
    
    def run(self):
        quadruples = self.quadruples
        while(self.solving < len(quadruples)):
            self.execute(quadruples[self.solving], self.memory, self.manager)
            self.solving += 1
            
    
    def execute(self, quadruple, memory, manager):
        oper, left_op, right_op, result = quadruple
        # if()
        print(f'{self.solving}\t{oper}\t{left_op}\t{right_op}\t{result}\n')
        if oper == '=':
                print(f'\t\t\t\t\tresult_address: {result}\tcurrent_value: {memory[result]}\tassigning: {manager.getValue(left_op)}')
                manager.setValue(result, manager.getValue(left_op))
                print(f'\t\t\t\t\tresult_address: {result}\tassigning: {manager.getValue(left_op)}\t\tassigned: {memory[result]}')

        elif oper in ['+', '-', '*', '/', '==', '>', '<', '!=', '>=', '<=']:
            valueL = manager.getValue(left_op)
            valueR = manager.getValue(right_op)

            # if(valueL == None or valueR == None):
            #     print(valueL, valueR)
            #     print(left_op)
            #     print(oper)
            #     piinkkLoader.stopExecution('Variable withouth value')
            
            if oper == '+':
                manager.setValue(result, valueL + valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')

            elif oper == '-':
                manager.setValue(result, valueL - valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')

            elif oper == '*':
                manager.setValue(result, valueL * valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')

            elif oper == '/':
                manager.setValue(result, valueL / valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')

            elif oper == '==':
                manager.setValue(result, valueL == valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')
            
            elif oper == '>':
                manager.setValue(result, valueL > valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')

            elif oper == '<':
                manager.setValue(result, valueL < valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')
            
            elif oper == '!=':
                manager.setValue(result, valueL != valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')
            
            elif oper == '>=':
                manager.setValue(result, valueL >= valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')
            
            elif oper == '<=':
                manager.setValue(result, valueL <= valueR)
                print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')
        
        elif oper == 'print':
            if isinstance(result, str):
                print(result)
                print(f'\t\t\t\t\tPRINTING {result}')
            else:
                print(manager.getValue(result))
                print(f'\t\t\t\t\tResult:{memory[result]}')

        elif oper == 'ERA':
            self.current_function = result
            print(result)
            # func = memory[function_name].value
            # args = []
            # for i in range(len(stack)):

        elif oper == 'PARAM':
            fun_name = self.current_function
            manager.setValue(result, manager.getValue(left_op))
            print(f'\t\t\t\t\tResult: {memory[result]}, {manager.getValue(result)}')
            # fun_info = self.symbol_table[fun_name]
            # parNO = int(result) - 1
            # par_type = fun_info['signature'][parNO]
            # parAddress = manager.getNewAddress('temp', par_type)
            # param = manager.getValue(left_op)
            # self.memory[parAddress] = param
            # print(f'en la ADDRESS {parAddress} WITH TYPE {par_type} STORED {param}')
        
        elif oper == 'GOSUB':
            # fun_name = left_op
            # fun_info = self.symbol_table[fun_name]
            # manager.getNewAddress('temp', 'int')
            # print(self.symbol_table[])
            self.stack.append(self.solving)
            self.solving = result - 1

        elif oper == 'GOTO':
            self.solving = result - 1

        elif oper == 'GOTOF':
            valueL = manager.getValue(left_op)
            if valueL == False:
                self.solving = result - 1

        elif oper == 'ENDFunc':
            salto = self.stack.pop()
            self.solving = salto
        # elif oper == 'RETURN':
        #     result_type = manager.getType(result)
        #     manager.getNewAddress('global', result_type)
        #     print(f'\t\t\t\t\tResult: {result}, {manager.getValue(result)}')
        #     # piinkkLoader.symbol_table['global']['variables'][piinkkLoader.current_scope] = 
        #     # print(piinkkLoader.symbol_table)
        #     print(manager.getValue(5004))
        #     # returnValAddress = piinkkLoader.symbol_table['global']['variables'][piinkkLoader.current_scope]['address']
        #     # manager.setValue(returnValAddress, manager.getValue(result))
        #     # memoryManager.memory[returnValAddress] = memoryManager.memory[value_address]
        #     # print(f'\t\t\t\t\tResult: {returnValAddress}, {manager.getValue(result)}')

    def handleEra(self, fun_name):
        fun_info = piinkkLoader.symbol_table[fun_name]



piinkk_vm = PiinkkVM(piinkkLoader.quadruples)
piinkk_vm.run()