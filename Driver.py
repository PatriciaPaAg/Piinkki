from antlr4 import *
from PiinkkLexer import PiinkkLexer
from PiinkkListener import PiinkkListener
from PiinkkParser import PiinkkParser
from ast import NodeTransformer 

test_valid_2 = """
Program Pelos;
VARS
    int i,j,k, arregl[10];
    float val;

function int fact (int j, float f, char c)
VAR
    int i;
{
    i = j + (p - j * 2 + j);
    if(j == 1){
        return(j);
    }else{
return(j * (j-1));
    }
}
main(){}
"""

tests = [test_valid_2]


for test in tests:
    print("--------------")
    print("Test: ", tests.index(test) + 1)
    lexer = PiinkkLexer(InputStream(test))
    stream = CommonTokenStream(lexer)
    parser = PiinkkParser(stream)
    tree = parser.prog()
    printer = PiinkkListener()
    walker = ParseTreeWalker()
    walker.walk(printer,tree)
    print(tree.toStringTree(recog=parser))

