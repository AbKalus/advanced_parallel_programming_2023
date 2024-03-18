""" Abdula Kalus SM3201269"""


from modules.operation import *


class Addition(BinaryOp):
    """
    Class that specializes the BnaryOp as Addition
    
    ...
    
    Attributes
    ----------
        symbol: default( + )
            Sum operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "+ "
    
    def op(self, *args):
        """Perform the operation addition
        
        Parameters
        ----------
            *args: float
                Allows us to pass a variable number of non-keyword arguments to the method
        
        Return
        ------
            float
                Result of the operation
        """
        res = 0
        for arg in args:
            res = res + arg
        return res


class Subtraction(BinaryOp):
    """
    Class that specializes the BnaryOp as Subtraction
    
    ...
    
    Attributes
    ----------
        symbol: default( - )
            Subtraction operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "- "

    def op(self, x, y):
        """Perform the operation subtraction
        
        Parameters
        ----------
            x: float
                First argument
            y: float
                Second argument
        Return
        ------
            float
                Result of the operation
        """
        return x-y


class Division(BinaryOp):
    """
    Class that specializes the BnaryOp as Division
    
    ...
    
    Attributes
    ----------
        symbol: default( / )
            Division operator
        
    Methods
    -------
        op(x, y):
            Perform the operation
    """
    symbol = "/ "

    def op(self, x, y):
        """Perform the operation division
        
        Parameters
        ----------
            x: float
                numerator
            y: float
                denominator
        
        Raises
        ------
            ZeroDivisionError
                If division is by zero raise exception
        
        Return
        ------
            float
                Result of the operation
        """
        try:
            return x/y
        except:
            raise ZeroDivisionException

    
class Multiplication(BinaryOp):
    """
    Class that specializes the BnaryOp as Multiplication
    
    ...
    
    Attributes
    ----------
        symbol: default( * )
            Multiplication operator
        
    Methods
    -------
        op(*args):
            Perform the operation
    """
    
    symbol = "* "
    
    def op(self, *args):
        """Perform the operation multiplication
        
        Parameters
        ----------
            *args: float
                Allows us to pass a variable number of non-keyword arguments to the method
        
        Return
        ------
            float
                Result of the operation
        """
        res = 1
        for arg in args:
            res = res * arg
        return res


class Power(BinaryOp):
    """
    Class that specializes the BnaryOp as Power
    
    ...
    
    Attributes
    ----------
        symbol: default( ** )
            Power operator
        
    Methods
    -------
        op(x, y):
            Perform the operation
    """
    symbol = "** "

    def op(self, x, y):
        """Perform the operation power
        
        Parameters
        ----------
            x: float
                base
            y: float
                exponent
        
        Return
        ------
            float
                Result of the operation
        """
        return x**y


class Modulus(BinaryOp):
    """
    Class that specializes the BnaryOp as Module
    
    ...
    
    Attributes
    ----------
        symbol: default( % )
            Module operator
    
    Methods
    -------
        op(x, y):
            Perform the operation
    """
    symbol = "% "

    def op(self, x, y):
        """Perform the operation module
        
        Parameters
        ----------
            x: float
                base
            y: float
                exponent
        
        Return
        ------
            float
                Result of the operation
        """
        return x%y


class Reciprocal(UnaryOp):
    """
    Class that specializes the UnaryOp as Reciporcal
    
    ...
    
    Attributes
    ----------
        symbol: default( 1/ )
            Reciprocal operator    
    
    Methods
    -------
        op(x):
            Perform the operation
    """
    
    symbol = "1/ "

    def op(self, x):
        """Perform the operation reciprocal
        
        Parameters
        ----------
            x: float
                base
        
        Return
        ------
            float
                Result of the operation
        """
        try:
            return 1/x
        except:
            raise ZeroDivisionException


class AbsoluteValue(UnaryOp):
    """
    Class that specializes the UnaryOp as AbsoluteValue
    
    ...
    
    Attributes
    ----------
        symbol: default( abs )
            AbsoluteValue operator    
    
    Methods
    -------
        op(x):
            Perform the operation
    """
    
    symbol = "abs "

    def op(self, x):
        """Perform the operation absolute value
        
        Parameters
        ----------
            x: float
                base
       
        Return
        ------
            float
                Result of the operation
        """
        return abs(x)
    