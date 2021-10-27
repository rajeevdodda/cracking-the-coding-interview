# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s: str) -> int:
    window = {}
    i = j = 0
    ans = 0

    while j < len(s):
        if s[j] not in window:
            window[s[j]]
            j += 1
            ans = max(ans, j - i)
        else:
            pass
            
        


print(lengthOfLongestSubstring("tmmzuxt"))
