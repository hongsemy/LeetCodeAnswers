from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """ Given an array of integers nums and an integer target, return
    indicies of the two numbers such that they add up to target.
    
    You may assume that each input would have exactly one solution,
    and you may not use the saem element twice.
    
    You can return the answer in any order.
    
    === Pre-condition ===
    - 2 <= len(nums) <= pow(10, 4)
    - (0 - pow(10, 9)) <= nums[i] <= pow(10, 9)
    - (0 - pow(10, 9)) <= target <= pow(10, 9)
    - Exactly onne valid answer exists
    
    Params
        nums(List[int]): A list that contains numbers
        target(int): A target sum of two numbers
    Return
        List[int]: Indicies of two numbers in a list which sum up to target
        
    >>> nums, target = [2, 7, 11, 15], 9 
    >>> two_sum(nums, target)
    [0, 1]
    >>> nums, target = [3, 2, 4], 6
    >>> two_sum(nums, target)
    [1, 2]
    >>> nums, target = [3, 3], 6
    >>> two_sum(nums, target)
    [0, 1]
    """
    for i in range(len(nums)):
        # Only check each numbers after index i.
        # Checking the sum of nums[i] and nums[i-n] for n >= 0 is redundent
        # since it must have been checked in the previous iteration
        # at least once.
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def two_sum_hash(nums: List[int], target: int) -> List[int]:
    """ Given an array of integers nums and an integer target, return
    indicies of the two numbers such that they add up to target.
    
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    
    You can return the answer in any order.
    
    === Pre-condition ===
    - 2 <= len(nums) <= pow(10, 4)
    - (0 - pow(10, 9)) <= nums[i] <= pow(10, 9)
    - (0 - pow(10, 9)) <= target <= pow(10, 9)
    - Exactly onne valid answer exists
    
    Params
        nums(List[int]): A list that contains numbers
        target(int): A target sum of two numbers
    Return
        List[int]: Indicies of two numbers in a list which sum up to target
        
    >>> nums, target = [2, 7, 11, 15], 9 
    >>> two_sum_hash(nums, target)
    [0, 1]
    >>> nums, target = [3, 2, 4], 6
    >>> two_sum_hash(nums, target)
    [1, 2]
    >>> nums, target = [3, 3], 6
    >>> two_sum_hash(nums, target)
    [0, 1]
    """
    hash_table = {}
    for i in range(len(nums)):
        # Insert key-value pairs into hash table. 
        # Since there is exactly one answer, there can't be three same values
        # in nums. Thus, using integers in nums as keys is acceptable.
        # Use indecies as values for hash table.
        hash_table[nums[i]] = i
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hash_table and hash_table[difference] != i:
            # If the difference between target and an individual number is
            # in hash table, it means the sum of two numbers is equal to
            # target.
            # The second statement makes sure that the same element is not
            # used twice.
            return [i, hash_table[difference]]
        

def two_sum_hash_two(nums: List[int], target: int) -> List[int]:
    """ Given an array of integers nums and an integer target, return
    indicies of the two numbers such that they add up to target.
    
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    
    You can return the answer in any order.
    
    === Pre-condition ===
    - 2 <= len(nums) <= pow(10, 4)
    - (0 - pow(10, 9)) <= nums[i] <= pow(10, 9)
    - (0 - pow(10, 9)) <= target <= pow(10, 9)
    - Exactly onne valid answer exists
    
    Params
        nums(List[int]): A list that contains numbers
        target(int): A target sum of two numbers
    Return
        List[int]: Indicies of two numbers in a list which sum up to target
        
    >>> nums, target = [2, 7, 11, 15], 9 
    >>> two_sum_hash(nums, target)
    [0, 1]
    >>> nums, target = [3, 2, 4], 6
    >>> two_sum_hash(nums, target)
    [1, 2]
    >>> nums, target = [3, 3], 6
    >>> two_sum_hash(nums, target)
    [0, 1]
    """
    hash_table = {}
    for i in range(len(nums)):
        # Check if the difference between target and nums[i] is in hash table.
        # Here we know for sure the same element is not used twice since
        # we check the existence of difference before inserting the element
        # that we are checking.
        difference = target - nums[i]
        if difference in hash_table:
            return [i, hash_table[difference]]
        # If such key value pair does not exist, insert nums[i] into hash table.
        hash_table[nums[i]] = i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
