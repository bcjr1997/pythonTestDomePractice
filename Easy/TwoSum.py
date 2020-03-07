def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    twoSumMap = dict()
    for index in range(len(numbers)):
        remainder = target_sum - numbers[index]
        twoSumMap[remainder] = index
    
    twoSumTuple = None

    for index in range(len(numbers)):
        if numbers[index] in twoSumMap and index != twoSumMap[numbers[index]]:
            twoSumTuple = (twoSumMap[numbers[index]], index)

    return twoSumTuple

print(find_two_sum([3, 0, 4, 4, 5, 0], 10))