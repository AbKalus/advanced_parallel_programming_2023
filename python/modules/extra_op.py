""" Abdula Kalus SM3201269"""


from modules.operation import *


class Print(UnaryOp):
    """
    Class that specializes the UnaryOp as Print
    
    Allows to print the evaluation of an expression
    
    ...
    
    Attributes
    ----------
        symbol: default ( print )
            Symbol for print
    
    Methods
    -------
        evaluate(env):
            Evaluate the expression
            Print the result and return the value of the evaluation
    """

    symbol = "print "
    
    def evaluate(self, env):
        """Evaluate the expression
        Print the result and return the value of the evaluation
        
        Parameters
        ---------- 
            env: dict
                Environment
        
        Return
        ------
            Any
                Return the value of the evaluation           
        """
        res = self.arg.evaluate(env)
        print(res)
        return res

    
class Nop(Operation):
    """
    Class that specializes the Operation as Nop
    
    It allows you to do nothing
    
    ...
    
    Attributes
    ----------
        arity: default ( 0 )
            No argument
    
    Methods
    -------
        evaluate(env):
            pass
    """
    arity = 0
    
    def evaluate(self, env):
        pass
    
    def __str__(self):
        """Override of the buildin method
        
        Return
        ------
            str
                String form for the Nop
        """
        return "(nop)"
