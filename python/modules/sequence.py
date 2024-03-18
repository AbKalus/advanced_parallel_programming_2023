""" Abdula Kalus SM3201269"""


from modules.operation import *


class Program(Operation):
    """
    Class that specializes the Operation as Program
    
    Allows to store and execute a sequence of expression
        
    ...
    
    Methods
    -------
        evaluate(env):
            Execute the expression and return the last executed
    """
    
    def __init__(self, args):
        """Constructor
        
        Get the attributes from the parent class and check for the arity of the program
        
        Parameters
        ---------
            args: list of Expression
            
        Raises
        ------
            SequenceException
                If the number of expression in the list don't coincide with the arity
                raise the excpetion
        """
        
        super().__init__(args)
    
    def evaluate(self, env):
        """Evaluates the expressions in the args list 
        and returns the value of the last evaluated expression
        
        Paramaters
        ----------
            env:
                Envirnonment
                
        Returns
        -------
            float or None
                return the last expressione performed
        """
        
        res = 0
        for expr in self.args: # [expr4, expr3, expr2, expr1]
            res = expr.evaluate(env)
        return res
    
        
    
     
    
class Prog2(Program):
    """
    Class that specializes the Progam as Prog2
    
    Allows to store and execute 2 expression
    
    ...
    
    Attributes
    ----------
        symbol: default( alloc )
            Symbol for the allocation of a variabile    
        arity: default ( 2 )
            Number of expression that cna be executed sequentially
    
    Methods
    -------
        evaluate(env):
            Execute the expression and return the last executed
    """
    
    symbol = "prog2 "
    arity = 2

    
class Prog3(Program):
    """
    Class that specializes the UnaryOp as Alloc
    
    Allows to store and execute 3 expression
    
    ...
    
    Attributes
    ----------
        symbol: default( alloc )
            Symbol for the allocation of a variabile    
        arity: default ( 3 )
            Number of expression that cna be executed sequentially
    
    Methods
    -------
        evaluate(env):
            Execute the expression and return the last executed
    """
    
    symbol = "prog3 "
    arity = 3
  
    
class Prog4(Program):
    """
    Class that specializes the UnaryOp as Alloc
    
    Allows to store and execute 2 expression
    
    ...
    
    Attributes
    ----------
        symbol: default( alloc )
            Symbol for the allocation of a variabile    
        arity: default ( 4 )
            Number of expression that cna be executed sequentially
    
    Methods
    -------
        evaluate(env):
            Execute the expression and return the last executed
    """
    
    symbol = "prog4 "
    arity = 4
    