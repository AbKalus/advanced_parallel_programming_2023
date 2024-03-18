""" Abdula Kalus SM3201269"""


from modules.expression import *
from modules.comparison_op import *
from modules.arithmetic_op import *
from modules.stack import *
from modules.variable_definition import *
from modules.sequence import *
from modules.condition_loop import *
from modules.subroutine import *
from modules.extra_op import *

d = {"+": Addition, "*": Multiplication, "**": Power, "-": Subtraction,
     "/": Division, "%": Modulus, "1/": Reciprocal, "abs": AbsoluteValue, 
     "=": Eq, "!=": Ne, ">": Gt, ">=": Ge, "<": Lt, "<=": Le,
     "alloc": Alloc, "valloc":Valloc, "setq": Setq, "setv": Setv,
     "prog2": Prog2, "prog3": Prog3, "prog4": Prog4,
     "if":If, "while": While, "for": For, "defsub": Defsub, "call": Call, "print": Print, "nop": Nop}
