
from antlr4 import *
from PiinkkLexer import PiinkkLexer
from PiinkkListenerExt import PiinkkListenerExt
from PiinkkParser import PiinkkParser
from piinkkLoader import piinkkLoader
from piinkkErrorListener import PiinkkErrorListener
from MemoryManage import memoryManage
from PiinkkVM import PiinkkVM

# Load the file
filename = 'test2.pink'
test = ''
with open(filename, 'r') as file:
    test = file.readlines()

# Create a lexer
lexer = PiinkkLexer(InputStream(''.join(test)))

# Create a token stream
stream = CommonTokenStream(lexer)

# Create a parser
parser = PiinkkParser(stream)

# Create an error listener
error_listener = PiinkkErrorListener()

# Remove the default error listener and add our custom one
parser.removeErrorListeners()
parser.addErrorListener(error_listener)

try: 
    # Parse the input
    tree = parser.prog()

    # Create a listener to process the parse tree
    listener = PiinkkListenerExt()

    # Walk the parse tree and trigger the appropriate listener methods
    ParseTreeWalker().walk(listener, tree)

    # Print the results
    print('\nPrints del main')
    print(piinkkLoader.operand_stack)
    print(piinkkLoader.type_stack)
    print(piinkkLoader.operator_stack)
    # contador = 0
    # for element in piinkkLoader.quadruples:
    #     print(piinkkLoader.quadruples[contador])
    #     contador += 1
    print(piinkkLoader.symbol_table)
    # print(piinkkLoader.quadruples)
    quadruples = piinkkLoader.quadruples
    virtualMachine = PiinkkVM()
    virtualMachine.quadruples = quadruples
    virtualMachine.run()
    # PiinkkVM.execute(quadruples)

except SyntaxError as e:
    # Print a syntax error message if a syntax error is encountered
    print(F'Syntax ERROR: {e}')

# Print a message to indicate the end of the program
print('hola mundo')
#
#This code loads a file, creates a lexer, token stream, parser, and listener, and then processes the file. If a syntax error is encountered, an error message is printed. Otherwise, the results of the processing are printed..</s>