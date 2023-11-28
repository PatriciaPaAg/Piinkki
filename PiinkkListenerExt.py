from antlr4 import *
from PiinkkListener import PiinkkListener
from piinkkLoader import piinkkLoader
from MemoryManage import memoryManage
from semanticCube import *

class PiinkkListenerExt(PiinkkListener):

    # Enter a parse tree produced by PiinkkParser#prog.
    def enterProg(self, ctx):
        print(memoryManage.globals)
        # print(memoryManage.globals['int']['iniAdd'])
        # print(memoryManage.globals['int']['finAdd'])
        # print(memoryManage.globals['int']['count'])

    # Exit a parse tree produced by PiinkkParser#prog.
    def exitProg(self, ctx):
        piinkkLoader.symbol_table = {}
        piinkkLoader.addQuadruple(['END', None, None, None])
        print(f'\t\t\tEND\t\t\tEND')
        

    # Enter a parse tree produced by PiinkkParser#programita0.
    def enterProgramita0(self, ctx):
        prog_info = ctx.getText()[7:]
        piinkkLoader.symbol_table['prog'] = {'name': prog_info, 'type': 'prog'}
        piinkkLoader.addQuadruple(['GOTO', None, None])
        print(f'\t\t\tGOTO\t\t\t_\t\t\tGOTO\t\t\t_')
                

    # Exit a parse tree produced by PiinkkParser#programita0.
    def exitProgramita0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#type0.
    def enterType0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#type0.
    def exitType0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#array0.
    def enterArray0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#array0.
    def exitArray0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#if0.
    def enterIf0(self, ctx):
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#if0.
    def exitIf0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#if1.
    def enterIf1(self, ctx):
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        PJumps = piinkkLoader.jump_stack
        exp_type = PilaT.pop()
        if exp_type == 'bool':
            result = PilaO.pop()
            result_address = piinkkLoader.getAddress(result)
            piinkkLoader.addQuadruple(['GOTOF', result_address, None])
            #print(f'{len(piinkkLoader.quadruples) - 1}')
            print(f'\t\t\tGOTOF\t{result}\t\t_\t\t\tGOTOF\t{result_address}\t\t_')
            PJumps.append(len(piinkkLoader.quadruples) - 1)
            #print('bool')
        else:
            piinkkLoader.stopExecution(f'Type mismatch: expecting bool') 


    # Exit a parse tree produced by PiinkkParser#if1.
    def exitIf1(self, ctx):
        PJumps = piinkkLoader.jump_stack
        end = PJumps.pop()
        #print('jump')
        #print(end)
        piinkkLoader.quadruples[end].append(len(piinkkLoader.quadruples) + 1)
        print(f'\t\t\t\t\t\t{piinkkLoader.quadruples[end]}')


    # Enter a parse tree produced by PiinkkParser#else0.
    def enterElse0(self, ctx):
        PJumps = piinkkLoader.jump_stack
        piinkkLoader.addQuadruple(['GOTO', None, None])
        #print(f'{len(piinkkLoader.quadruples) - 1}')
        print(f'\t\t\tGOTO\t\t\t_\t\t\tGOTO\t\t\t_')
        inCase_false = PJumps.pop()
        #print('jump')
        #print(inCase_false)
        PJumps.append(len(piinkkLoader.quadruples) - 1)
        piinkkLoader.quadruples[inCase_false].append(len(piinkkLoader.quadruples) + 1)
        print(f'\t\t\t\t\t\t{piinkkLoader.quadruples[inCase_false]}')

    # Exit a parse tree produced by PiinkkParser#else0.
    def exitElse0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#while0.
    def enterWhile0(self, ctx):
        piinkkLoader.jump_stack.append(len(piinkkLoader.quadruples) + 1)

    # Exit a parse tree produced by PiinkkParser#while0.
    def exitWhile0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#while1.
    def enterWhile1(self, ctx):
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        PJumps = piinkkLoader.jump_stack
        exp_type = PilaT.pop()
        if exp_type == 'bool':
            result = PilaO.pop()
            result_address = piinkkLoader.getAddress(result)
            piinkkLoader.addQuadruple(['GOTOF', result_address, None])
            print(f'\t\t\tGOTOF\t{result}\t\t_\t\t\tGOTOF\t{result_address}\t\t_')
            PJumps.append(len(piinkkLoader.quadruples) - 1)
            #print('bool')
        else:
            piinkkLoader.stopExecution(f'Type mismatch: expecting bool') 

    # Exit a parse tree produced by PiinkkParser#while1.
    def exitWhile1(self, ctx):
        PJumps = piinkkLoader.jump_stack
        end = PJumps.pop()
        returne = PJumps.pop()
        #print(f'end -> {end}')
        #print(f'returne -> {returne}')
        piinkkLoader.addQuadruple(['GOTO', None, None, returne])
        print(f'\t\t\tGOTO\t\t\t{returne}\t\t\tGOTO\t\t\t{returne}\t\t')
        piinkkLoader.quadruples[end].append(len(piinkkLoader.quadruples) + 1)
        print(f'\t\t\t\t\t\t{piinkkLoader.quadruples[end]}')


    # Enter a parse tree produced by PiinkkParser#for0.
    def enterFor0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#for0.
    def exitFor0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#var0.
    def enterVar0(self, ctx):
        var_info = ctx.getText()
        piinkkLoader.operand_stack.append(var_info)
        # AQUI SE PUEDE PONER LO DE LOS NUMEROS ENTEROS O FLOAT
        if piinkkLoader.isNumber(var_info) == 'int':
            piinkkLoader.type_stack.append('int')
            if piinkkLoader.getAddress(var_info) == None:
                number_address = memoryManage.getNewAddress('ctes', 'int')
                piinkkLoader.symbol_table['cte']['variables'][var_info] = {'type': 'int', 'address': number_address}
        elif piinkkLoader.isNumber(var_info) == 'float':
            piinkkLoader.type_stack.append('float')
            if piinkkLoader.getAddress(var_info) == None:
                number_address = memoryManage.getNewAddress('ctes', 'float')
                piinkkLoader.symbol_table['cte']['variables'][var_info] = {'type': 'float', 'address': number_address}
        else:
            var_type = piinkkLoader.getType(var_info)
            piinkkLoader.type_stack.append(var_type)
        #print('Operand Stack')
        #print(piinkkLoader.operand_stack)

    # Exit a parse tree produced by PiinkkParser#var0.
    def exitVar0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#vars0.
    def enterVars0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#vars0.
    def exitVars0(self, ctx):
        pass


    def enterVars1(self, ctx):
        vars_info = ctx.getText().split(':')
        vars_type, vars_info = vars_info[0], vars_info[1].split(',')
        scope = piinkkLoader.current_scope
        for var_info in vars_info:
            #  If the next element is an array
            if '[' in var_info:
                var_name, var_arr_size = var_info.split('[')
                var_arr_size = int(var_arr_size.rstrip(']'))
                piinkkLoader.variableCheck(var_name)
                piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': vars_type, 'size': var_arr_size}
            else:
                var_name = var_info
                piinkkLoader.variableCheck(var_name)
                address = memoryManage.getNewAddress(scope, vars_type)
                #print(f'AAAAAAAAADDDDDDDDREEEEEEEEEESSSSSSSS {address}, {var_name}, {vars_type} \t ')
                piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': vars_type, 'address': address}            

    # Exit a parse tree produced by PiinkkParser#vars1.
    def exitVars1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#expresion0.
    def enterExpresion0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#expresion0.
    def exitExpresion0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#expresion1.
    def enterExpresion1(self, ctx):
        operator_info = ctx.getText()
        for operator in ['==', '>', '<', '!=', '>=', '<=']:
            if operator in operator_info:
                piinkkLoader.operator_stack.append(operator)

    # Exit a parse tree produced by PiinkkParser#expresion1.
    def exitExpresion1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#exp0.
    def enterExp0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#exp0.
    def exitExp0(self, ctx):
        Poper = piinkkLoader.operator_stack
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        if Poper:
            if Poper[-1] in ['==', '>', '<', '!=', '>=', '<=']:
                right_operand = PilaO.pop()
                right_type = PilaT.pop()
                left_operand = PilaO.pop()
                left_type = PilaT.pop()
                operator = Poper.pop()
                result_type = semantic_cube[left_type][right_type][operator]
                #print(result_type)
                if(result_type == PiinkkError):
                    piinkkLoader.stopExecution(f'Type mismatch >') 

                temporal = 't' + str(piinkkLoader.getTemporal())
                PilaO.append(temporal)
                PilaT.append(result_type)
                right_address = piinkkLoader.getAddress(right_operand)
                left_address = piinkkLoader.getAddress(left_operand)
                temporal_address = memoryManage.getNewAddress('temp', result_type)
                piinkkLoader.symbol_table['temp']['variables'][temporal] = {'type': result_type, 'address': temporal_address}  
                piinkkLoader.addQuadruple([operator, left_address, right_address, temporal_address])
                print(f'\t\t\t{operator}\t{left_operand}\t{right_operand}\t{temporal}\t\t\t{operator}\t{left_address}\t{right_address}\t{temporal_address}\t\t\t{operator}\t{left_type}\t{right_type}\t{result_type}')
                piinkkLoader.temporal += 1


    # Enter a parse tree produced by PiinkkParser#exp1.
    def enterExp1(self, ctx):
        operator = ctx.getText()[0]
        piinkkLoader.operator_stack.append(operator)

    # Exit a parse tree produced by PiinkkParser#exp1.
    def exitExp1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#termino0.
    def enterTermino0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#termino0.
    def exitTermino0(self, ctx):
        Poper = piinkkLoader.operator_stack
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        if Poper:
            if Poper[-1] in ['+', '-']:
                right_operand = PilaO.pop()
                right_type = PilaT.pop()
                left_operand = PilaO.pop()
                left_type = PilaT.pop()
                operator = Poper.pop()
                result_type = semantic_cube[left_type][right_type][operator]
                #print(result_type)
                if(result_type == PiinkkError):
                    piinkkLoader.stopExecution(f'Type mismatch +')
                temporal = 't' + str(piinkkLoader.getTemporal())
                PilaO.append(f'{temporal}')
                PilaT.append(result_type)
                right_address = piinkkLoader.getAddress(right_operand)
                left_address = piinkkLoader.getAddress(left_operand)
                temporal_address = memoryManage.getNewAddress('temp', result_type)
                piinkkLoader.symbol_table['temp']['variables'][temporal] = {'type': result_type, 'address': temporal_address}
                piinkkLoader.addQuadruple([operator, left_address, right_address, temporal_address])
                print(f'\t\t\t{operator}\t{left_operand}\t{right_operand}\t{temporal}\t\t\t{operator}\t{left_address}\t{right_address}\t{temporal_address}\t\t\t{operator}\t{left_type}\t{right_type}\t{result_type}')
                piinkkLoader.temporal += 1
    

    # Enter a parse tree produced by PiinkkParser#termino1.
    def enterTermino1(self, ctx):
        operator = ctx.getText()[0]
        piinkkLoader.operator_stack.append(operator)

    # Exit a parse tree produced by PiinkkParser#termino1.
    def exitTermino1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#factor0.
    def enterFactor0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#factor0.
    def exitFactor0(self, ctx):
        Poper = piinkkLoader.operator_stack
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        if Poper:
            if Poper[-1] in ['*', '/']:
                right_operand = PilaO.pop()
                right_type = PilaT.pop()
                left_operand = PilaO.pop()
                left_type = PilaT.pop()
                operator = Poper.pop()
                result_type = semantic_cube[left_type][right_type][operator]
                #print(result_type)
                if(result_type == PiinkkError):
                    piinkkLoader.stopExecution(f'Type mismatch *') 
                temporal = 't' + str(piinkkLoader.getTemporal())
                PilaO.append(temporal)
                PilaT.append(result_type)
                right_address = piinkkLoader.getAddress(right_operand)
                left_address = piinkkLoader.getAddress(left_operand)
                temporal_address = memoryManage.getNewAddress('temp', result_type)
                piinkkLoader.symbol_table['temp']['variables'][temporal] = {'type': result_type, 'address': temporal_address}  
                piinkkLoader.addQuadruple([operator, left_address, right_address, temporal_address])
                print(f'\t\t\t{operator}\t{left_operand}\t{right_operand}\t{temporal}\t\t\t{operator}\t{left_address}\t{right_address}\t{temporal_address}\t\t\t{operator}\t{left_type}\t{right_type}\t{result_type}')
                piinkkLoader.temporal += 1


    # Enter a parse tree produced by PiinkkParser#bloque0.
    def enterBloque0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#bloque0.
    def exitBloque0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#estatuto0.
    def enterEstatuto0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#estatuto0.
    def exitEstatuto0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#asignacion0.
    def enterAsignacion0(self, ctx):
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#asignacion0.
    def exitAsignacion0(self, ctx):
        assignTo = ctx.getText().split('=')[0]
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        assignThis = PilaO.pop()
        assignThis_type = PilaT.pop()
        assignTo_type = piinkkLoader.getType(assignTo)
        operator = '='
        result_type = semantic_cube[assignTo_type][assignThis_type][operator]
        assignThis_address = piinkkLoader.getAddress(assignThis)
        assignTo_address = piinkkLoader.getAddress(assignTo)
        # print(PilaO)
        # print(result_type)
        # print(assignTo_type, assignThis_type, operator)
        if(result_type == PiinkkError):
            piinkkLoader.stopExecution(f'Type mismatch =') 
        piinkkLoader.addQuadruple([operator, assignThis_address, None, assignTo_address])
        print(f'\t\t\t{operator}\t{assignThis}\t\t{assignTo}\t\t\t{operator}\t{assignThis_address}\t\t{assignTo_address}\t\t\t{operator}\t{assignThis_type}\t{assignTo_type}\t{result_type}')
        


    # Enter a parse tree produced by PiinkkParser#escritura0.
    def enterEscritura0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#escritura0.
    def exitEscritura0(self, ctx):
        pass


   # Enter a parse tree produced by PiinkkParser#escri.
    def enterEscri1(self, ctx):
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#escri.
    def exitEscri1(self, ctx):
        impre = piinkkLoader.operand_stack.pop()
        impre_type = piinkkLoader.type_stack.pop()
        impre_address = piinkkLoader.getAddress(impre)
        piinkkLoader.addQuadruple(['print', None, None, impre_address])
        print(f'\t\t\tprint\t\t\t{impre}\t\t\tprint\t\t\t{impre_address}')

    def enterEscri2(self, ctx):
        impre = ctx.getText()[1:-1]
        piinkkLoader.addQuadruple(['print', None, None, impre])
        print(f'\t\t\tprint\t\t\t{impre}')

    # Exit a parse tree produced by PiinkkParser#escri.
    def exitEscri2(self, ctx):
        pass


# Enter a parse tree produced by PiinkkParser#lectura0.
    def enterLecturaInt0(self, ctx):
        leido = ctx.getText().split('(')[1][:-2]
        #print(leido)
        piinkkLoader.addQuadruple(['read', None, None, leido])
        print(f'\t\t\tread\t\t\t{leido}')
        piinkkLoader.variableCheck(leido)
        leido_address = memoryManage.getNewAddress(piinkkLoader.current_scope, 'int')
        piinkkLoader.symbol_table[piinkkLoader.current_scope]['variables'][leido] = {'type': 'int', 'address': leido_address}
        piinkkLoader.pendientes.append('cambiar enterLectura a constantes enteras')

    # Exit a parse tree produced by PiinkkParser#lectura0.
    def exitLecturaInt0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#return0.
    def enterReturn0(self, ctx):
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#return0.
    def exitReturn0(self, ctx):
        value = piinkkLoader.operand_stack.pop()
        value_type = piinkkLoader.type_stack.pop()
        value_address = piinkkLoader.getAddress(value)
        piinkkLoader.addQuadruple(['RETURN', None, None, value_address])
        print(f'\t\t\tRETURN\t\t\t{value}\t\t\tRETURN\t\t\t{value_address}')


    # Enter a parse tree produced by PiinkkParser#fun0.
    def enterFun0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#fun0.
    def exitFun0(self, ctx):
        scope = piinkkLoader.current_scope
        firstTemp = piinkkLoader.symbol_table[scope]['noTemp']
        #print(f'TEMPORAAAAAAALLLLL INICIAAAA {firstTemp}')
        calcTemp = piinkkLoader.temporal - firstTemp
        #print(f'TEMPORAAAAAAALLLLL FINALIZAA  {piinkkLoader.temporal}')
        piinkkLoader.symbol_table[scope]['noTemp'] = calcTemp
        piinkkLoader.addQuadruple(['ENDFunc', None, None, None])
        print(f'\t\t\tENDFunc\t\t\t\t\t\tENDFunc')
        piinkkLoader.symbol_table[scope]['variables'] = {}
        piinkkLoader.set_current_scope('global')
        memoryManage.resetCountLocal()
        memoryManage.resetCountTemp()


    # Enter a parse tree produced by PiinkkParser#fun1.
    def enterFun1(self, ctx):
        print('ENTRA A FUNCION')
        piinkkLoader.clearStacks()
        fun_info = ctx.getText().split(':')
        fun_type, fun_name = fun_info[0], fun_info[1].split('(')[0]
        piinkkLoader.functionCheck(fun_name)
        tempCalc = piinkkLoader.temporal
        piinkkLoader.symbol_table[fun_name] = {'type': fun_type, 'start': 0,'variables': {}, 'signature': [], 'noParam': 0, 'noVar': 0, 'noTemp': tempCalc}
        piinkkLoader.set_current_scope(fun_name)

    # Exit a parse tree produced by PiinkkParser#fun1.
    def exitFun1(self, ctx):
        scope = piinkkLoader.current_scope
        signature = piinkkLoader.symbol_table[scope]['signature']
        piinkkLoader.symbol_table[scope]['noParam'] = len(signature)
        

    # Enter a parse tree produced by PiinkkParser#fun2.
    def enterFun2(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#fun2.
    def exitFun2(self, ctx):
        pass

    # Enter a parse tree produced by PiinkkParser#fun3.
    def enterFun3(self, ctx):
        var_info = ctx.getText().split(':')
        var_type, var_info = var_info[0], var_info[1]
        scope = piinkkLoader.current_scope
        #  If the next element is an array
        if '[' in var_info:
            var_name, var_arr_size = var_info.split('[')
            var_arr_size = int(var_arr_size.rstrip(']'))
            piinkkLoader.variableCheck(var_name)
            piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': var_type, 'size': var_arr_size}
            piinkkLoader.symbol_table[scope]['signature'].append(var_type)
        else:
            var_name = var_info
            piinkkLoader.variableCheck(var_name)
            address = memoryManage.getNewAddress(scope, var_type)
            #print(f'AAAAAAAAADDDDDDDDREEEEEEEEEESSSSSSSS {address}, {var_name}, {var_type} \t ')     
            piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': var_type, 'address': address}
            piinkkLoader.symbol_table[scope]['signature'].append(var_type)

    # Exit a parse tree produced by PiinkkParser#fun3.
    def exitFun3(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#funContent0.
    def enterFunContent0(self, ctx):
        scope = piinkkLoader.current_scope
        nVar = len(piinkkLoader.symbol_table[scope]['variables'])
        nParam = piinkkLoader.symbol_table[scope]['noParam']
        piinkkLoader.symbol_table[scope]['noVar'] = nVar - nParam
        piinkkLoader.symbol_table[scope]['start'] = len(piinkkLoader.quadruples) + 1
        # print(piinkkLoader.symbol_table[scope]['start'])

    # Exit a parse tree produced by PiinkkParser#funContent0.
    def exitFunContent0(self, ctx):
        pass


# Enter a parse tree produced by PiinkkParser#funCall0.
    def enterFunCall0(self, ctx):
        piinkkLoader.clearStacks()
        fun_name = ctx.getText().split('(')[0]
        fun_type = piinkkLoader.symbol_table[fun_name]['type']
        # if fun_type != 'void':
        #     piinkkLoader.stopExecution(f'Return type: {fun_type}, must be used in an operation')
        piinkkLoader.functionCallCheck(fun_name)
        piinkkLoader.current_fun = fun_name
        piinkkLoader.addQuadruple(['ERA', None, None, fun_name])
        print(f'\t\t\tERA\t\t\t{fun_name}\t\t\tERA\t\t\t{fun_name}')
        #piinkkLoader.param_count += 1
        # print('PARAAAAAAMMMM COUUUUUUNTTTTTTTTTT')
        # print(piinkkLoader.param_count)
        #piinkkLoader.symbol_table[

    # Exit a parse tree produced by PiinkkParser#funCall0.
    def exitFunCall0(self, ctxt):
        fun = piinkkLoader.current_fun
        #piinkkLoader.param_count += 1
        parameter_count = piinkkLoader.param_count 
        signature = piinkkLoader.symbol_table[fun]['signature']
        if parameter_count + 1 < len(signature):
            piinkkLoader.stopExecution(f'Missing arguments')
        iniAddr = piinkkLoader.symbol_table[fun]['start']
        piinkkLoader.addQuadruple(['GOSUB', fun, None, iniAddr])
        print(f'\t\t\tGOSUB\t{fun}\t\t{iniAddr}\t\t\tGOSUB\t{fun}\t\t{iniAddr}')
        piinkkLoader.set_param_count(0)
        fun = ''        


    # Enter a parse tree produced by PiinkkParser#funCall1.
    def enterFunCall1(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#funCall1.
    def exitFunCall1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#funCallExp.
    def enterFunCallExp(self, ctxt):
        piinkkLoader.param_count += 1

    # Exit a parse tree produced by PiinkkParser#funCallExp.
    def exitFunCallExp(self, ctx):
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        fun = piinkkLoader.current_fun
        argument = PilaO.pop()
        argument_type = PilaT.pop()
        parameter_count = piinkkLoader.param_count
        signature = piinkkLoader.symbol_table[fun]['signature']
        # print(parameter_count)
        if parameter_count > len(signature):
            piinkkLoader.stopExecution(f'Too many arguments')
        parameter_type = piinkkLoader.symbol_table[fun]['signature'][parameter_count - 1]
        argument_address = piinkkLoader.getAddress(argument)
        # print('ARGUMEEEEEENT TYPEEEEEEE')
        # print(argument)
        # print(argument_type)
        # print('PARAAAAAAMMMM TYPEEEEEEE')
        # print(parameter_count)
        # print(parameter_type)
        if parameter_type == argument_type:
            piinkkLoader.addQuadruple(['PARAM', argument, None, f'par{parameter_count}'])
            print(f'\t\t\tPARAM\t{argument}\t\tpar{parameter_count}\t\t\tPARAM\t{argument_address}\t\tpar{parameter_count}')
        else:
            piinkkLoader.stopExecution(f'Function signature mismatch: expecting {parameter_type}')



    # Enter a parse tree produced by PiinkkParser#funCall2.
    def enterFunCall2(self, ctx):
        #piinkkLoader.param_count += 1
        pass

    # Exit a parse tree produced by PiinkkParser#funCall2.
    def exitFunCall2(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#body0.
    def enterBody0(self, ctx):
        piinkkLoader.quadruples[0].append(len(piinkkLoader.quadruples) + 1)
        print(f'\t\t\t\t\t\t{piinkkLoader.quadruples[0]}')
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#body0.
    def exitBody0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#start.
    def enterStart(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#start.
    def exitStart(self, ctx):
        pass
