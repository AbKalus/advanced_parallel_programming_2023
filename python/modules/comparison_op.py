""" Abdula Kalus SM3201269"""


from modules.operation import *


class Eq(BinaryOp):
    """
    Class that specializes the BinaryOp as Equality
    
    ...
    
    Attributes
    ----------
        symbol: default( = )
            Equality operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "= "
    
    def op(self, x, y):
        """Equality operation
        
        Check if the x is equal to y
        
        Parameters
        ----------
            x: float
                first argument
            y: float
                second argument
        
        Return
        ------
            float
                Result of the operation
        """
        return x==y


class Ne(BinaryOp):
    """
    Class that specializes the BinaryOp as Unequality
    
    ...
    
    Attributes
    ----------
        symbol: default( != )
            Unequality operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "!= "
    
    def op(self, x, y):
        """Unequality operation
        
        Check if the x is unequal to y
        
        Parameters
        ----------
            x: float
                first argument
            y: float
                second argument
        
        Return
        ------
            float
                Result of the operation
        """
        return x!=y

    
class Gt(BinaryOp):
    """
    Class that specializes the BinaryOp as Greater Than
    
    ...
    
    Attributes
    ----------
        symbol: default( > )
            Greater Than operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "> "
    
    def op(self, x, y):
        """Greater Than operation
        
        Check if the x is greater than y
        
        Parameters
        ----------
            x: float
                first argument
            y: float
                second argument
        
        Return
        ------
            float
                Result of the operation
        """
        return x>y


class Ge(BinaryOp):
    """
    Class that specializes the BinaryOp as Greater Than or Equal
    
    ...
    
    Attributes
    ----------
        symbol: default( >= )
            Greater Than or Equal operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = ">= "
    
    def op(self, x, y):
        """Greater Than or Equal operation
        
        Check if the x is greater than y or is equal to y
        
        Parameters
        ----------
            x: float
                first argument
            y: float
                second argument
        
        Return
        ------
            float
                Result of the operation
        """
        return x>=y


class Lt(BinaryOp):
    """
    Class that specializes the BinaryOp as Less Than
    
    ...
    
    Attributes
    ----------
        symbol: default( < )
            Less Than operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "< "
    
    def op(self, x, y):
        """Less Than operation
        
        Check if the x is less than y
        
        Parameters
        ----------
            x: float
                first argument
            y: float
                second argument
        
        Return
        ------
            float
                Result of the operation
        """
        return x<y


class Le(BinaryOp):
    """
    Class that specializes the BinaryOp as Less Than or Equal
    
    ...
    
    Attributes
    ----------
        symbol: default( <= )
            Less Than or Equal operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "<= "
    
    def op(self, x, y):
        """Greater Than or Equal operation
        
        Check if the x is greater than y or is equal to y
        
        Parameters
        ----------
            x: float
                first argument
            y: float
                second argument
        
        Return
        ------
            float
                Result of the operation
        """
        return x<=y
