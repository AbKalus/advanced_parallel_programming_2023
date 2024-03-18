""" Abdula Kalus SM3201269"""


class EmptyStackException(Exception):
    """ 
    Check if there is something to pop from the stack
    """
    
    def __str__(self) -> str:
        return "Nothing to pop from the stack"


class BadInputStringExcaption(Exception):
    """ 
    If cerating the expression something goes wrong raise excaption
    """
    def __str__(self) -> str:
        return "String passed to create the expression isn't correctly formulated"


class MissingVariableException(Exception):
    """ 
    If the enviroment assignemnt isn't a number raise exception
    """
    
    def __str__(self) -> str:
        return "If the enviroment assignemnt isn't a number raise Exception"


class ZeroDivisionException(Exception):
    """ 
    Can't divide by zero
    """
    
    def __str__(self) -> str:
        return "Can't divide by zero"

    
class DimOfArrayWrongException(Exception):
    """
    The dimension of the array to allocate is wrong
    """
    
    def __str__(self) -> str:
        return "The dimension of the array to allocate is wrong"

class DuplicateVariableException(Exception):
    """
    The variable already exists
    """
    
    def __str__(self) -> str:
        return "The variable already exists, can't be duplicated"