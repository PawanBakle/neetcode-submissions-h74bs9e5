class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # create a set and 
        # for every occurences create the key as the element

        # u_number = {}
        # for i in range(len(nums)):
        #     num = u_number.get(nums[i],0)
        #     if not u_number.get(nums[i],None):
        #         u_number[nums[i]] = nums[i]
        #     else:
        #         continue
        # return len(list(u_number))
        if not nums:
            return 0
        i = 0
        for next_num in range(1, len(nums)):
            if nums[next_num] != nums[i]:
                i += 1 # i comes with j
                nums[i] = nums[next_num] # put value of nums at j in nums[i]

        return i + 1




