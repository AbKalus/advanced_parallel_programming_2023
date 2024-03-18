""" Abdula Kalus SM3201269"""


from modules.operation import *


class Defsub(BinaryOp):
    """
    Class that specialize the BinaryOp as Defsub
    
    Allows to define an expression as a subroutine stored in the env
    
    ...
    
    Attributes
    ----------
        symbol: default ( defsub )
            Symbol for subroutine
    
    Methods
    -------
        evaluate(env):
            Store in the env the expression in arg2 called with arg1 name 
    """
    symbol = "defsub "
    
    def evaluate(self, env):
        """Store in the env the expression in arg2 
        called with arg1 name
        
        Parameters
        ----------
            env: dict
                Environment
        """
        var_name = self.arg1.name
        env[var_name] = self.arg2


class Call(UnaryOp):
    """
    Class that specialize the BinaryOp as Call
    
    Allows to call a subroutine stored in the env
    
    ...
    
    Attributes
    ----------
        symbol: default ( call )
            Symbol for call
    
    Methods
    -------
        evaluate(env):
            Store in the env the expression in arg2 called with arg1 name 
    """
    
    symbol = "call "
    
    def evaluate(self, env):
        """Call the subroutine with name arg for evaluation
        
        Parameters
        ----------
            env: dict
                Environment
        
        Returns
        -------
            float
                Value of the subroutine evaluation
        """
        var_name = self.arg.name
        res = env[var_name].evaluate(env) 
        return res
