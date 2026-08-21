class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(arr, start, end):
            pivot = arr[end]
            i = start - 1

            for j in range(start, end):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            return i + 1

        def quick_select(arr, start, end):
            if start == end:
                return arr[start]

            pivot = partition(arr, start, end)

            if pivot == len(nums) - k:
                return arr[pivot]
            elif pivot > len(nums) - k:
                return quick_select(arr, start, pivot - 1)
            else:
                return quick_select(arr, pivot + 1, end)

        return quick_select(nums, 0, len(nums) - 1)
