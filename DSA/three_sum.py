# Three Sum dynamic problem solution
def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num1 in enumerate(nums):

            if i > 0 and num1 == nums[i-1]:
                continue

            start, end = i+1, len(nums) - 1

            while start < end:
                sum = num1 + nums[start] + nums[end]

                if sum > 0:
                    end -= 1
                elif sum < 0:
                    start += 1
                else:
                    res.append([num1, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1

        return res