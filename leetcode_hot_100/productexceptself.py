class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Calculate the product of all elements to the left of each index
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        # Calculate the product of all elements to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output