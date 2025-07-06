nums = [1,0,-1,0,-2,2]
target = 0

class Solution(object):
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                start = j+1
                end = len(nums)-1
                while start < end:
                    current = nums[i] + nums[j] + nums[start] + nums[end]
                    if current == target:
                        ans.add((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                    elif current<target:
                        start +=1
                    elif current>target:
                        end -=1
        return list(nums)
sol=Solution()
print(sol.fourSum(nums, target))