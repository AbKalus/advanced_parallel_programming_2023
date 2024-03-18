""" Abdula Kalus SM3201269"""


from modules.operation import *


class Alloc(UnaryOp):
    """
    Class that specializes the UnaryOp as Alloc
    
    ...
    
    Attributes
    ----------
        symbol: default( alloc )
            Symbol for the allocation of a variabile    
    
    Methods
    -------
        evaluate(env):
            Add the variable to the environment
    """
    symbol = "alloc "
        
    def evaluate(self, env):
        """Allocate a variabile in the environment
        
        Parameters
        ----------
            env: dict
                Environment in which to add the variable
        """
        var_name = self.arg.name
        env[var_name] = 0

    
class Valloc(BinaryOp):
    """
    Class that specializes the BinaryOp as Valloc
    
    ...
    
    Attributes
    ----------
        symbol: default( valloc )
            Symbol for the allocation of an array    
        
    Methods
    -------
        evaluate(env):
            Add the array to the environment
    """
    
    symbol = "valloc "
            
    def evaluate(self, env):
        """Add the array to the environment
        
        Parameters
        ----------
            env: dict
                Environment in which to add the variable
        """
        try:
            var_name = self.arg1.name
            lst = [0]*int(self.arg2.evaluate(env))
            env[var_name] = lst
        except:
            raise DimOfArrayWrongException
    

class Setq(BinaryOp):
    """
    Class that specializes the BinaryOp as Setq
    
    ...
    
    Attributes
    ----------
        symbol: default( setq )
            Symbol for the setting the value of a variable    
        
    Methods
    -------
        evaluate(env):
            Set/Update the variable of the environment
    """
    
    symbol = "setq "
        
    def evaluate(self, env):
        """Set/Update the value of a variable
        
        Parameters
        ----------
            env: dict
                Environment where to update the variable
                
        Return
        ------
            float
                Value assigned to the variable
        """
        var_name = self.arg1.name
        value = self.arg2.evaluate(env)
        env[var_name] = value
        return value
        
    
class Setv(TernaryOp):
    """
    Class that specializes the TernaryOp as Setv
    
    ...
    
    Attributes
    ----------
        symbol: default( setv )
            Set a vlaue of the array in the environment    
    
    Methods
    -------
        evaluate(env):
            Set/Update an element of the array of the environment
    """
    
    symbol = "setv "

    def evaluate(self, env):
        """Set/Update a vlaue of the array in the environment
        
        Parameters
        ----------
            env: dict
                Environment where to update the variable
        
        Return
        ------
            float
                Value assigned to the element of the array
        """
        var_name = self.arg1.name
        idx = int(self.arg2.evaluate(env))
        expr_eval = self.arg3.evaluate(env)
        env[var_name][idx] = expr_eval        
        return expr_eval