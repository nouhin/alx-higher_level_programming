#!/usr/bin/python3
def weight_average(my_list=[]):
    """Function that returns the weighted average of all integers tuple (<score>, <weight>)
    """
    denominator = sum([x[1] for x in my_list])
    numerator = sum([x[0] * x[1] for x in my_list])
    return numerator / denominator if denominator else 0
