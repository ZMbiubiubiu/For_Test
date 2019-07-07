"""
求众数

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。
"""

# method 1.map映射法
#  找出数组中每个数出现的次数
#  输出次数最多的那个

# method 2.排序法
#  要找的元素一定在排序之后序列的中间位置
class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        Solution.quick_sort(nums)
        return nums[len(nums) // 2]

    @staticmethod
    def quick_sort(nums):
        if nums is None or len(nums) == 0:
            return nums
        low, high = 0, len(nums) - 1
        Solution.sort(nums, low, high)

    @staticmethod
    def sort(nums, low, high):
        if low >= high:
            return
        mid = Solution.partition(nums, low, high)
        Solution.sort(nums, low, mid - 1)
        Solution.sort(nums, mid + 1, high)

    @staticmethod
    def partition(nums, low, high):
        flag = nums[low]
        left = low + 1
        right = high
        while 1:
            while nums[left] <= flag and left < high:
                left += 1
            while nums[right] >= flag and right > low:
                right -= 1
            if left >= right:
                break
            Solution.swap(nums, left, right)
        Solution.swap(nums, low, right)
        return right

    @staticmethod
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# method 3.投票法
#  累计同一值，记做目标值，出现的次数，遍历整个数组，如果发现当前值与目标值不同
#  判断times是否大于1，如果大于1，则在当前的times-1.目标值还是以前的目标值
#  如果times不大于1，将当前值换成目标值，继续遍历
class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        target = None
        times = 0
        for num in nums:
            if num == target:
                times += 1
            else:
                if times > 1:
                    times -= 1
                else:
                    target = num
                    times = 1
        return target