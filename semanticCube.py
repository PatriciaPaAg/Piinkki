# Def de operadores
# Aritméticos * / + -  
# Relacionales < > <= >= == !=
# Lógicos ! (NOT) & (AND) | (OR) 
# Asignación = += -=
# Incremento y decremento ++ --

PiinkkError = 'TypeError'

semantic_cube = {
    'int':{
        'int':{
            '*': 'int',
            '/': 'float',
            '+': 'int',
            '-': 'int',
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'int',
        },
        'float':{
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': PiinkkError,
        },
        'bool':{
            '*': PiinkkError,
            '/': PiinkkError,
            '+': PiinkkError,
            '-': PiinkkError,
            '<': PiinkkError,
            '>': PiinkkError,
            '<=': PiinkkError,
            '>=': PiinkkError,
            '==': PiinkkError,
            '!=': PiinkkError,
            '=': PiinkkError,
        },
    },

    'float':{
        'int':{
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': PiinkkError,
        },
        'float':{
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'float',
        },
        'bool':{
            '*': PiinkkError,
            '/': PiinkkError,
            '+': PiinkkError,
            '-': PiinkkError,
            '<': PiinkkError,
            '>': PiinkkError,
            '<=': PiinkkError,
            '>=': PiinkkError,
            '==': PiinkkError,
            '!=': PiinkkError,
            '=': PiinkkError,
        },
    },

    'bool':{
        'int':{
            '*': PiinkkError,
            '/': PiinkkError,
            '+': PiinkkError,
            '-': PiinkkError,
            '<': PiinkkError,
            '>': PiinkkError,
            '<=': PiinkkError,
            '>=': PiinkkError,
            '==': PiinkkError,
            '!=': PiinkkError,
            '=': PiinkkError,
        },
        'float':{
            '*': PiinkkError,
            '/': PiinkkError,
            '+': PiinkkError,
            '-': PiinkkError,
            '<': PiinkkError,
            '>': PiinkkError,
            '<=': PiinkkError,
            '>=': PiinkkError,
            '==': PiinkkError,
            '!=': PiinkkError,
            '=': PiinkkError,
        },
        'bool':{
            '*': PiinkkError,
            '/': PiinkkError,
            '+': PiinkkError,
            '-': PiinkkError,
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'bool',
        },
    },
}


def cubo(operand1, operand2, operator):
    return semantic_cube[operand1][operand2][operator]