class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = None
        for i in nums:
            k = nums.index(i)
            for j in nums[k+1:]:
                if (j+i)== target:
                    return [k, nums[k+1:].index(j)+k+1]
                    
            

        return [0,0]