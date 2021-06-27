# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


def threeSome(nums):
    ans = []
    nums.sort()

    for idx, value in enumerate(nums):
        if idx > 0 and value == nums[idx - 1]:
            continue
        l, r = idx + 1, len(nums) - 1
        while l < r:
            threesome = value + nums[l] + nums[r]
            if threesome > 0:
                r -= 1
            elif threesome < 0:
                l -= 1
            else:
                ans.append([value, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return ans


print(threeSome([-1,-2,0,4,3,1]))