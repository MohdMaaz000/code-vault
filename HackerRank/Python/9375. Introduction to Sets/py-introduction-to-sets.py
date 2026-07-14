def average(array):

    distinct_heights = set(array)
    
    return sum(distinct_heights) / len(distinct_heights)

