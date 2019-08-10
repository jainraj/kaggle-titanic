from math import log
from functools import reduce


def base2_log(value):
    """Wrapper over math.log to handle 0 input"""
    return 0 if value == 0 else log(value, 2)


def entropy(series):
    """Shannon entropy of the series"""
    value_counts = series.value_counts()
    full_sum = sum(value_counts)
    ratios = map(lambda x: x / full_sum, value_counts)
    return reduce(lambda run,ele: run - ele * base2_log(ele), ratios, 0)


def uniqueness(series):
    """Number of unique values as a fraction of length of the series"""
    return series.nunique() / len(series)


def completeness(series):
    """Ratio of non-null entries"""
    return series.count() / len(series)
