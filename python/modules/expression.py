""" Abdula Kalus SM3201269"""


from modules.stack import *
from modules.additional_exception import *


class Expression:
    """
    This class defines Reverse Polish notation
    
    Is a mathematical notation in which operators follow their operands, 
    in contrast to prefix or Polish notation, in which operators precede their operands
    
    ...
    
    Attributes
    ----------
        __stack:
            LIFO data strcutre where the expressions are stored
    
    Methods
    -------
        @classmethod from_program(cls, text, d)
            Class method that creates the expression starting from a text string
        
        evaluate(env)
            Method that evaluates the expression starting from an environment containing
            the assignments to the variables
    """

    def __init__(self):
        """Constructor
        
        Initialize an empty expression
        """
        self.__stack = Stack()

    @classmethod
    def from_program(cls, text, disptach):
        """Class method that creates the expression starting from a text string
        
        Must be given the text to create the associated expression and 
        the disptach dict to assign the correct operation
        
        Parameters
        ----------
            text: str
                String that represent as expression
                
            disptach: dict
                Associate the operation to the correct class representation
                
        Raises
        ------
            BadInputStringExcaption
                If cerating the expression something goes wrong, there are symbol not allowd raise excaption
                e.g. a_1, /, £ ecc..
                
        Return
        ------
            Expression object
                Representation of the given string as an RPN expression 
        """
        expr = cls()                    # create an instance of the class
        items = text.split()
        for i in items:                 # core of the method, create the expression
            if i in disptach.keys():    # if the itme in the list is an operation
                op_lst = []
                [op_lst.append(expr.__stack.pop()) for _ in range(disptach[i].arity)]  # extract from the stack the argument needed for the operation
                expr.__stack.push(disptach[i](op_lst))      # push to the stack the new object 
            elif i.isalnum():                               # if the item is alphanumeric
                if i.isalpha():                             # it's a variable if it is a variable
                    expr.__stack.push(Variable(i))
                elif isinstance(float(i), float):               # it's a constant if it is a number
                    expr.__stack.push(Constant(i))
            else:
                raise BadInputStringExcaption
            
        return expr
            
    def evaluate(self, env):
        """Evaluates the expression starting from an environment containing
        the assignments to the variables
        
        Parameters
        ----------
            env: dict
                Environment
            
        Return
        ------
            float
                Value of the evaluated expression
        """
        return self.__stack.pop().evaluate(env)
    
    def __str__(self):
        """Override of the buildin method
        
        Return
        ------
            str
                String form for the expression
        """
        return str(self.__stack)
    

class Variable(Expression):
    """
    Class that specializes the Expression as Variable
    
    ...
    
    Attributes
    ----------
        name: str
            Name of the varible
        
    Methods
    -------
        evaluate(env)
            Evaluate the variable
    """

    def __init__(self, name):
        """Construct
        
        Initialize the attributes of the object
        
        Parameters
        ----------
            name: str
                Name of the variable
        """
        self.name = name

    def evaluate(self, env):
        """Evaluate the variable
        
        Based on the enviroment assignment returns the value assigned
        
        Parameters
        ----------
            env: dict
                Environment
        
        Raises
        ------
            VariableValueException
                If the enviroment assignemnt isn't a number or an rray raise exception
        
        Return
        ------
            float
                Evaluation of the variable
        """
        res = env[self.name]
        try:
            if isinstance(res, list):
                return res
            else:
                return float(res)
        except:
            raise MissingVariableException

    def __str__(self):
        """Override of the buildin method
        
        Return
        ------
            str
                String form for the variable
        """
        return str(self.name)


class Constant(Expression):
    """
    Class that specializes the Expression as Constant
    
    ...
    
    Attributes
    ----------
        value: str
            Value of the constant
        
    Methods
    -------
        evaluate(env)
            Evaluate the constant
    """
    
    def __init__(self, value):
        """Constructor
        
        Initialize the attributes of the object
        
        Parameters
        ----------
            value: float
                Value of the constant
        """
        self.value = value

    def evaluate(self, env):
        """Evaluate the constant
        
        Parameters
        ----------
            env: dict
                Environment
        
        Return
        ------
            float
                Evaluation of the constant
        """
        return float(self.value)

    def __str__(self):
        """Override of the buildin method
        
        Return
        ------
            str
                String form for the constant
        """
        return str(self.value)
