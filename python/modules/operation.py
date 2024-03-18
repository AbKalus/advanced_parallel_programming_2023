""" Abdula Kalus SM3201269"""


from modules.expression import *


class Operation(Expression):
    """
    Class that specializes the Expression as Operation
    
    ...
    
    Attributes
    ----------
        symbol: str
            Default value is ?, used to represent the symbol of the operation
        
        args: list
            List of arguments passed for the operation
        
    Methods
    -------
        evaluate(env)
            pass
    
        op(*args)
            NotImplementeError
    """

    symbol = '? '
    
    def __init__(self, args):
        """Constructor
        
        Initialize the attributes of the object
        
        Parameters
        ---------
            args: list
                Arguments used for the operation
        """
        self.args = args

    def evaluate(self, env):
        """Do nothing         
        """
        pass

    def op(self, *args):
        """Do nothing
        
        Raises
        ------
            NotImplementedError
                If this method is called raise an exception beacuse it isn't implemented
        """
        raise NotImplementedError()

    def __str__(self):
        """Override of the buildin method
        
        Return
        ------
            str
                String form for the operation
        """
        return f"({self.symbol}{' '.join(str(arg) for arg in self.args)})"

class QuaternaryOp(Operation):
    """
    Class that specializes the Operation as QuaternaryOp
    
    Operation with four arguments
    
    ...
    
    Attributes
    ----------
        arity: int
            Default value is 4, number of arguments needed for the operation
            
        arg1, arg2, arg3, arg4: Constant, Variable or Operation
            Arguments of the operation
        
    Methods
    -------
        evaluate(env)
            Evaluate the operation
    """
    
    arity = 4
    
    def __init__(self, args):
        """Constructor
        
        Initialize the attributes of the object
        
        Parameters
        ---------
            args: list of Constant, Variable and Operation
                - arg1: first argument
                - arg2: second argument
                - arg3: third argument
                - arg4: fourth argument
        """
        super().__init__(args)
        (self.arg1, self.arg2, self.arg3, self.arg4) = self.args


class TernaryOp(Operation):
    """
    Class that specializes the Operation as TernaryOp
    
    Operation with three arguments
    
    ...
    
    Attributes
    ----------
        arity: int
            Default value is 3, number of arguments needed for the operation
            
        arg1, arg2, arg3: Constant, Variable or Operation
            Arguments of the operation
        
    Methods
    -------
        evaluate(env)
            Evaluate the operation
    """
    
    arity = 3
    
    def __init__(self, args):
        """Constructor
        
        Initialize the attributes of the object
        
        Parameters
        ---------
            args: list of Constant, Variable and Operation
                - arg1: first argument
                - arg2: second argument
                - arg3: third argument
        """
        super().__init__(args)
        (self.arg1, self.arg2, self.arg3) = self.args



class BinaryOp(Operation):
    """
    Class that specializes the Operation as BinaryOp
    
    Operation with two arguments
    
    ...
    
    Attributes
    ----------
        arity: int
            Default value is 2, number of arguments needed for the operation
            
        arg1, arg2: Constant, Variable or Operation
            Arguments of the operation
        
    Methods
    -------
        evaluate(env)
            Evaluate the operation
    """
    
    arity = 2
    
    def __init__(self, args):
        """Constructor
        
        Initialize the attributes of the object
        
        Parameters
        ---------
            args: list of Constant, Variable and Operation
                - arg1: first argument
                - arg2: second argument
        """
        super().__init__(args)
        (self.arg1, self.arg2) = self.args
    
    def evaluate(self, env):
        """Evaluate a bianry operation
        
        Parameters
        ----------
            env: dict
                Environment
        
        Return
        ------
            float
                Return the result of the operation
        """
        x = self.arg1.evaluate(env)
        y = self.arg2.evaluate(env)
        return self.op(x, y)


class UnaryOp(Operation):
    """
    Class that specializes the Operation as UnaryOp
    
    Operation with one argument
    
    ...
    
    Attributes
    ----------
        arity: int
            Default value is 2, number of arguments needed for the operation
            
        arg: Constant, Variable or Operation
            Argument of the operation
        
    Methods
    -------
        evaluate(env)
            Evaluate the operation
    """
    
    
    arity = 1
    
    def __init__(self, args):
        """Constructor
        
        Initialize the attributes of the object
        
        Parameters
        ---------
            arg: Constant, Variable or Operation
                Argument of the operation
        """
        super().__init__(args)
        (self.arg) = self.args[0]
        
    def evaluate(self, env):
        """Evaluate the operation
        
        Parameters
        ----------
            env: dict
                Environment
        
        Return
        ------
            float
                Return the result of the operation
        """
        x = self.arg.evaluate(env)
        return self.op(x)
