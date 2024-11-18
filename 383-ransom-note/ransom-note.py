class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        for char in ransomNote:
            if char in magazine:
                ransomNote = ransomNote.replace(char,'',1)
                magazine = magazine.replace(char,'',1)
        
        if ransomNote == "":
            return True
        else:
            return False