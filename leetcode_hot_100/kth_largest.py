class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from random import randint
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            division_gap = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[division_gap], nums[i] = nums[i], nums[division_gap]
                    division_gap += 1

            nums[right], nums[division_gap] = nums[division_gap], nums[right]
            return division_gap
        
        def quickselect(left, right, k_smallest):
            if left == right:
                return nums[left]
            else:
                pivot_index = randint(left, right)
                pivot = nums[pivot_index]
                gap = partition(left, right, pivot_index)

                if gap == k_smallest:
                    return pivot
                elif gap < k_smallest:
                    return quickselect(gap + 1, right, k_smallest)
                else:
                    return quickselect(left, gap - 1, k_smallest)
                
        size = len(nums)
        return quickselect(0, size - 1, size - k)
    #使用这种方法处理大量相同元素时会变成O(n^2)，可以考虑使用三路快排来优化
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from random import randint
        target = len(nums) - k
        def triple_partition(left, right):
            pivot = nums[randint(left, right)]
            left_pointer = left
            equal_pointer = left
            right_pointer = right

            while equal_pointer <= right_pointer:
                if nums[equal_pointer] < pivot:
                    nums[left_pointer], nums[equal_pointer] = nums[equal_pointer], nums[left_pointer]
                    left_pointer += 1
                    equal_pointer += 1
                elif nums[equal_pointer] > pivot:
                    nums[right_pointer], nums[equal_pointer] = nums[equal_pointer], nums[right_pointer]
                    right_pointer -= 1
                else:
                    equal_pointer += 1

            if target < left_pointer:
                return triple_partition(left, left_pointer - 1)
            elif target > right_pointer:
                return triple_partition(right_pointer + 1, right)
            else:
                return nums[target]
            
        return triple_partition(0, len(nums) - 1)