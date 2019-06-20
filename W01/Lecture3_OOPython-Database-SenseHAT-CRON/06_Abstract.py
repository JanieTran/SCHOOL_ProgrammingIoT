# you will need a module ABC

from abc import ABC, abstractmethod
 
 
class AbstractOperation(ABC):
 
    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()
    
    # this is called as a decorator

    @abstractmethod
    def execute(self):
        pass

# children

class AddOperation(AbstractOperation):
    def execute(self):
        return self.operand_a + self.operand_b
 
 
class SubtractOperation(AbstractOperation):
    def execute(self):
        return self.operand_a - self.operand_b
 
 
class MultiplyOperation(AbstractOperation):
    def execute(self):
        return self.operand_a * self.operand_b
 
 
class DivideOperation(AbstractOperation):
    def execute(self):
        return self.operand_a / self.operand_b

# now you can write some code to print values