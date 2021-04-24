class SimpleOperations:

    def __init__(self, firstNumber, secondNumber):
        self.first_number = firstNumber
        self.second_number = secondNumber

    def sum(self):
        return self.first_number + self.second_number

    def difference(self):
        return self.first_number - self.second_number

    def divide(self):
        if self.second_number > 0:
            return self.first_number / self.second_number
        else:
            return "second number should be greater than 0"

    def multiply(self):
        return self.first_number * self.second_number
