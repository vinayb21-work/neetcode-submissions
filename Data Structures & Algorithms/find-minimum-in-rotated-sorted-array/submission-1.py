class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = float("inf")
        if nums[low] < nums[high]:
            return nums[low]        
        while low <= high:
            mid = (low + high) // 2
            print("low", low, "high", high, "mid", mid)
            ans = min(ans, nums[mid])
            if nums[low] < nums[high]:
                high = mid - 1
            else:
                if nums[mid] < nums[low]:
                    if nums[high] < nums[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    if nums[low] < nums[high]:
                        high = mid - 1
                    else:
                        low = mid + 1
        return ans

                

# 6 1 2 3 4 5