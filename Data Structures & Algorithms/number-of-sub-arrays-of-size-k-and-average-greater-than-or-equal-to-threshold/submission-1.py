class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        left = 0

        for r in range(k - 1, len(arr)):
            sums = 0
            for i in range(left, r + 1):
                sums += arr[i]

            if sums / k >= threshold:
                res += 1
            left += 1

        return res