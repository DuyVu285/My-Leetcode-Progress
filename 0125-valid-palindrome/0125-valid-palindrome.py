class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = s.replace(" ","").lower()
        txt = re.sub(r'[^a-zA-Z0-9]', '', txt)
        
        return txt == txt[::-1]
