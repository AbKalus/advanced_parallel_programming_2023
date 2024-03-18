""" Abdula Kalus SM3201269"""


from modules.additional_exception import *


class Stack:
    """
    Class that represent a stack data structure
    
    ...
        
    Attributes
    ----------
        data: lst
            public attribute taht represents data structure stack
        
    Methods
    -------
        push(x)
            Add an element to the stack
            
        pop()
            Return the last element
            
        stack_len()
            Return the number of elements in the stack 
    """

    def __init__(self):
        """Constructor
        
        Initialize an empty stack
        """
        self.data = []

    def push(self, x):
        """Add an element to the stack
        
        Must pass the argument x
        
        Parameters
        ----------
            x: Any
                Add an operation, variable or constant object to the stack
        """
        self.data.append(x)

    def pop(self):
        """Return the last element

        Raises
        ------
            EmptyStackException
                If the stack is empty
        
        Returns
        -------
            Any
                An object of types Operation, Variable and Constant
        """
        if self.data == []:
            raise EmptyStackException
        res = self.data[-1]
        self.data = self.data[0:-1]
        return res

    def stack_len(self):
        """Return the number of elements in the stack

        Returns
        -------
            int
                Number of object in the stack
        """
        return len(self.data)
    
    def __str__(self):
        """Override of the buildin method
        
        Return
        ------
            str
                Representation of the stack
        """
        return " ".join([str(s) for s in self.data])
