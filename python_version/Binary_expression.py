import Arithmetic_expression
import Arithmetic_op

#TODO how do i make this class implement arithmetic_expression

class Binary_expression():
    def __init__(self, op, expr1, expr2):
        if op == None:
            raise TypeError("null arithmetic operator argument");
        if expr1 == None or expr2 == None:
            raise TypeError("null expression argument");
        self.expr1 = expr1;
        self.expr2 = expr2;
        self.op = op;

    def evaluate(self):

        value = 0
        if self.op == add_operator:
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == mul_operator:
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == div_operator:
            value = self.expr1.evaluate() / self.expr2.evaluate()
        elif self.op == sub_operator:
            value = self.expr1.evaluate() - self.expr2.evaluate()
        return value