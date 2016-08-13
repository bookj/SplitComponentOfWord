# def add(num1, num2):
#     return num1 + num2
#

# 1+1
# 2
# 2+2
# 4
#    2-2
# 0

class Calculator():
    def __init__(self, expression):
        print("Starting calculator.. ")
        self.expression = expression
        self.operator = self.define_operator()

    # function -- split with '+'
    def split_by_plus(self):
        return self.expression.split("+")

    def split_by_minus(self):
        return self.expression.split("-")

    def convert_list_string_to_int(self, list_string):

        return [
            int(list_string[0]),
            int(list_string[1])
            ]

    # function -- convert to integer
    def calculate_list_int(self, list_int):
        if self.operator == "+":
            return list_int[0] + list_int[1]
        elif self.operator == "-":
            return list_int[0] - list_int[1]
        return None

    def define_operator(self):
        if "+" in self.expression:
            self.operator = "+"
        elif "-" in self.expression:
            self.operator = "-"
        else:
            self.operator = None
        return self.operator

    def calculate(self):
        # split_result = self.split_by_plus(string)
        # oper = self.define_operator(string)
        if self.operator is not None:
            if self.operator == '+':
                split_result = self.split_by_plus()
            elif self.operator == '-':
                split_result = self.split_by_minus()

            convert_result = self.convert_list_string_to_int(split_result)
            return self.calculate_list_int(convert_result)

if __name__ == '__main__':
    input_data = input("Enter your expression: ")
    print(Calculator(input_data).calculate())
