class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        sol = None
        for i, val in enumerate(nums):
            if target<=val:
                sol = i 
                break
            
        return sol if sol is not None else i+1