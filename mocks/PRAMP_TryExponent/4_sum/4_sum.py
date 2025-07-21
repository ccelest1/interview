class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # sort input
        nums.sort()
        # vars used in recursive function
        """
        res stores all quads we need to return
        quad stores current quadruplet building
        """
        res, quad = [], []

        """
        k - value is going to be decremented in order to understand what next elements we need to look for and how many
            * base case being 2
        start - starting index we are observing
        target - will change as we continue to pick values
        """

        def kSum(k, start, target):
            # non-base case
            if k != 2:
                # subtract k from len(nums) (+1 as it is non inclusive)
                # need at least k values left in order to perform picks
                for i in range(start, len(nums) - k + 1):
                    # avoid duplicates (redundant indices),
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            # base case, two sum ii
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    # prevent duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        kSum(4, 0, target)
        return res


s = Solution()
# [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

# [[2,2,2,2]]
print(s.fourSum([2, 2, 2, 2, 2], 8))
