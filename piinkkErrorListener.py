from tracemalloc import start
from antlr4.error.ErrorListener import ErrorListener

class PiinkkErrorListener(ErrorListener):
    """
    Custom Error Listener for Piinkk.

    This class extends the ErrorListener class from the ANTLR4 library.
    It overrides the syntaxError method to raise a SyntaxError with a custom error message.
    """
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Override the syntaxError method from the ErrorListener class.

        This method is called when a syntax error is encountered during the parsing process.
        It raises a SyntaxError with a custom error message that includes the line and column number of the error.

        :param recognizer: The recognizer where the error occurred.
        :param offendingSymbol: The offending symbol that caused the error.
        :param line: The line number where the error occurred.
        :param column: The column number where the error occurred.
        :param msg: The error message.
        :param e: The exception that was thrown.
        """
        raise SyntaxError(f"line {line}:{column} {msg}")
