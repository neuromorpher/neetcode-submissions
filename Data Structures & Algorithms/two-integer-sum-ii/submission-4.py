class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        cache = {}
        for i in range(n-1):

            reach = target - numbers[i]

            cache[reach] = i  

            if numbers[i+1] in cache.keys():

                return [cache[numbers[i+1]] + 1, i+2]




         