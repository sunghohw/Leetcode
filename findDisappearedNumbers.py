def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    num_set = set(nums)
    for i in xrange(1,len(nums)+1):
        if i not in num_set: result.append(i)
    return result
