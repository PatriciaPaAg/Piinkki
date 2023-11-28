
from MemoryManage import MemoryManage
from piinkkLoader import piinkkLoader

class PiinkkVM:
    def __init__(self):
        self.quadruples = []
        self.symbol_table = piinkkLoader.symbol_table
        self.stack = []   # Stack for managing function calls and expressions
        self.count = 0

    # def printQuadruples(self):
    #     quadruples = self.quadruples
    #     for quadruple in quadruples:
    #         print(quadruple)
    
    def run(self):
        quadruples = self.quadruples
        while(self.count < len(quadruples)):
            self.execute(quadruples[self.count])
            self.count += 1
            
    
    def execute(self, quadruple):
        oper, left_op, right_op, result = quadruple
        # print(self.count + 1)
        # print(f'\t{quadruple}')
        print(f'{self.count + 1}\t{oper}\t{left_op}\t{right_op}\t{result}')
        # print('esta entrando')
        if (oper == '='):
            self.symbol_table.g


# quadruples = piinkkLoader.quadruples

piinkk_vm = PiinkkVM()
piinkk_vm.run()   