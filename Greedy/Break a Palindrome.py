class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pal = list(palindrome)
        start = 0
        end = len(pal) - 1
        if len(pal) == 1:
            return ""
        while start < end:
            if pal[start] == 'a' and pal[end] == 'a':
                start += 1
                end -= 1
            elif pal[start] != 'a':
                pal[start] = 'a'
                return "".join(pal)
        if pal[-1] == 'a':
            pal[-1] = 'b'
            return "".join(pal)
        return ""
                