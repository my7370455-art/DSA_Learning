class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        prev = None
        nums.sort()
        anticipated_length = len(nums) // 2 + 1
        count = 0
        for i in nums:
            if i != prev or prev is None:
                if count >= anticipated_length:
                    return prev
                prev = i
                count = 1
            else:
                count += 1

        return prev