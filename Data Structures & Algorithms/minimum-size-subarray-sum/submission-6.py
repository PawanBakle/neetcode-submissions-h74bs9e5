class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0,0
        ex_len = 0
        m_len = 0
        min_len = float('inf')
        n = len(nums)
        while right < n:
            ex_len += nums[right]
            right += 1 
            m_len += 1
            while ex_len >= target:
                min_len = min(m_len,min_len)
                m_len -= 1
                ex_len -= nums[left]
                left += 1
                
                # if ex_len <= target:
                    
                #     break
                
            

        
        if min_len == float('inf'):
            return 0
        return min_len