class Solution:
    """
    U: 
      I: Funtion takes in a list of number and a target
      O: Excpected to return a list of indices. the numbers in the indices should sum up to target.

    P: 
     
     Use a hashmap that stores each index with it's value
     loop through each index and check if their value sums up to target.
     if they do, return the list

    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # 3 : 0, 4: 1
        for i,val in enumerate(nums):
            if target - val in d:
                return [d[target - val],i]
            else:
                d[val] = i



        



        