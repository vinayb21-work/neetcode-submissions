from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache    
        def check(curr):
            # print("curr", curr)
            if curr == "":
                return True
            
            for word in wordDict:
                if curr.startswith(word):
                    if check(curr[len(word):]):
                        return True

            return False
        
        return check(s)