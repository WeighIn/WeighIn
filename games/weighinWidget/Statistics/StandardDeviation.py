__author__ = 'Radhir'
import Statistics

final_list = []
list_in_values = []
in_value = 0
# RESTRICTIONS
# FOR VERY 1st VALUE, VALUE IS SIMPLY ADDED TO FINALLIST AND NO COMPUTATION IS DONE SINCE VARIANCE = UNDEFINED
# CALCULATE T-DISTRIBUTION FROM 2nd VALUE ON
#SWITCH TO NORMAL STANDARD-DEVIATION AFTER REACHING 30 SCORES
class WeighInBackend:
    def __init__(self, in_val):
        self.in_value = in_val
        list_in_values.append(in_val)

    def calculate(self, in_val):
        if len(list_in_values) == 0:
            list_in_values.append(in_val)
            final_tuple = (in_value, 0)
            final_list.append(final_tuple)
        if len(list_in_values) >= 1:
            self.t_distribution(in_val)
        if len(list_in_values) > 30:
            self.standardDeviation(in_val)

    def mean(self,in_val):
        return Statistics.mean(list_in_values)

    def median(self,in_val):
        return Statistics.median(list_in_values)

    def t_distribution(in_value):
        list_square_values = []

        #Computes sum of all values in list and then squares this value and divides by number of elements in list
        sum_of_values_squared = (sum(list_in_values) ** 2) / len(list_in_values)

        for i in range(len(list_in_values)):
            #Squares each individual value and adds to list
            temp_square_value = (list_in_values[i]) ** 2
            list_square_values.append(temp_square_value)

        #Calculates ss_value by summing individual value squared from the sum_values_squared
        ss_value = sum(list_square_values) - sum_of_values_squared

        #Calculates standard deviation by taking square root of variance
        t_value = (ss_value / (len(list_in_values) - 1)) ** 0.5

        final_tuple = (in_value, t_value)
        final_list.append(final_tuple)

        return final_tuple

    def standard_deviation(in_value):
        list_square_values = []
        average = sum(list_in_values) / len(list_in_values)

        for i in range(len(list_in_values)):
            temp_square_value = (list_in_values[i] - average) ** 2
            list_square_values.append(temp_square_value)

        standard_dev_value = sum(list_square_values) / (len(list_in_values))
        standard_dev_value **= 0.5

        #Create a tuple and add it to a list of all records
        final_tuple = (in_value, standard_dev_value)
        final_list.append(final_tuple)

        for i in final_list:
            print i

        return final_tuple