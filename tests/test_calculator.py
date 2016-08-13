import unittest

from simple_calculator.calculator import Calculator

# class AddTest(unittest.TestCase):
#
#     def add_1_1_should_be_2_test(self):
#         assert add(1,1) == 2

class SplitByPlusTest(unittest.TestCase):

    def split_1_plus_1_should_be_list_of_1_1_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_3_plus_5_should_be_list_of_3_5_test(self):
        assert Calculator("3+5").split_by_plus() == ['3','5']

    def split_1_plus_2_should_be_list_of_1_2_test(self):
        assert Calculator("1+2").split_by_plus() == ['1','2']

class SplitByMinusTest(unittest.TestCase):

    def split_1_minus_2_should_be_list_of_1_2_test(self):
        assert Calculator("1-2").split_by_minus() == ['1','2']

    def split_3_minus_4_should_be_list_of_3_4_test(self):
        assert Calculator("3-4").split_by_minus() == ['3','4']

    def split_5_minus_6_should_be_list_of_5_6_test(self):
        assert Calculator("5-6").split_by_minus() == ['5','6']

class ConvertListStringToIntTest(unittest.TestCase):

    def convert_list_of_1_1_string_to_1_1_int_test(self):
        assert Calculator("1+1").convert_list_string_to_int(['1','1']) == [1,1]

class CalculateListIntTest(unittest.TestCase):

    def calculate_list_of_1_plus_1_int_should_be_2_test(self):
        assert Calculator("1+1").calculate_list_int([1,1]) == 2
    def calculate_list_of_1_minus_1_int_should_be_2_test(self):
        assert Calculator("1-1").calculate_list_int([1,1]) == 0

class DefineOperatorTest(unittest.TestCase):

    def define_operator_1_plus_1_should_be_plus_test(self):
        assert Calculator("1+1").define_operator() == "+"

    def define_operator_1_minus_1_should_be_minus_test(self):
        assert Calculator("1-1").define_operator() == "-"

    def define_operator_1_1_should_be_none_test(self):
        assert Calculator("11").define_operator() == None

class CalculateTest(unittest.TestCase):

    def calculate_string_1_plus_1_should_be_2_test(self):
        assert Calculator("1+1").calculate() == 2

    def calculate_string_4_minus_3_should_be_1_test(self):
        assert Calculator("4-3").calculate() == 1
