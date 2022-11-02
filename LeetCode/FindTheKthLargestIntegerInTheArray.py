class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        return sorted(nums, key=lambda num: int(num))[-k]
        
