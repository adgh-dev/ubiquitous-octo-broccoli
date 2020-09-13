def twoSum(nums, target):
        pair_sum = {}
        for i in range(0, len(nums)):
            print(pair_sum)
            diff = target - nums[i]
            print(diff)
            if i in pair_sum:
                return [pair_sum[i], i]
            else:
                pair_sum[diff] = i
        return pair_sum


print(
    twoSum([2,7,11,15], 9)
)