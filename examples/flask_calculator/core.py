class Calculator(object):
    def __init__(self):
        pass
    def add(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2