""" Abdula Kalus SM3201269 """


from modules.operation import *


class If(TernaryOp):
    """
    Class that specializes the TernaryOp as If
    
    Allows to execute one of the two branches of the construct
        
    ...
    
    Attributes
    ----------
    symbol: default ( if )
        if istruction
    
    Methods
    -------
        evaluate(env):
            Execute the expression and returns arg2 
            if the condition is true and arg3 if it is false
    """
    
    symbol = "if "
        
    def evaluate(self, env):
        """Execute the expression and returns arg2 
            if the condition is true and arg3 if it is false
            
        Parameters
        ----------
            env: dict
                Environment
        
        Returns
        -------
            Any:
                The value of the branch of the if that was evaluated is returned 
        """
        flag = self.arg1.evaluate(env)
        if flag:
            return self.arg2.evaluate(env)
        else:
            return self.arg3.evaluate(env)

        
class While(BinaryOp):
    """
    Class that specializes the BinaryOp as While
    
    Allows to execute an expressione while the condition is ture
        
    ...
    
    Attributes
    ----------
    symbol: default ( while )
        while istruction
    
    Methods
    -------
        evaluate(env):
            Execute the expression and returns arg2 
            while the cond of arg1 is true
    """
    
    symbol = "while "
        
    def evaluate(self, env):
        """Execute the expression and returns arg2 
            while the cond of arg1 is true
            
        Parameters
        ----------
            env: dict
                Environment
        """
        flag = self.arg1.evaluate(env)
        res = 0
        while flag:
            res = self.arg2.evaluate(env)
            flag = self.arg1.evaluate(env)
        return res


class For(QuaternaryOp):
    """
    Class that specializes the QuaternaryOp as While
    
    Allows to execute an expression for n times
        
    ...
    
    Attributes
    ----------
    symbol: default ( for )
        for istruction
    
    Methods
    -------
        evaluate(env):
            Execute the expression from arg4 while arg1
            is between arg2 and arg3 
    """
    
    symbol = "for "
    
    def evaluate(self, env):
        """Execute the expression from arg4 while arg1
            is between arg2 and arg3 
            
        Parameters
        ----------
            env: dict
                Environment
                
        Raises
        ------
            DuplicateVariableException
                If the variable is already present in the environment raise exception
        """
        res = 0
        var_name = self.arg1.name
        if var_name in env:
            raise DuplicateVariableException
        start = int(self.arg2.evaluate(env))
        end = int(self.arg3.evaluate(env))
        expr = self.arg4
        env[var_name] = start
        for i in range(start, end):
            env[var_name] = i
            res = expr.evaluate(env)
        env.pop(var_name)
        return res
        