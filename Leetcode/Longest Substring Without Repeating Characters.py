class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sIdx = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in sIdx and sIdx[char] >= left:
                left = sIdx[char] + 1

            sIdx[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
    
main = Solution()
print(main.lengthOfLongestSubstring("dvdf"))