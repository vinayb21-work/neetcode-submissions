class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ans = []
        n = len(digits)
        if n == 0:
            return []
        
        def generate(curr, i):
            if i == n:
                ans.append("".join(curr[::]))
                return
            
            for char in mapping[digits[i]]:
                curr.append(char)
                generate(curr, i+1)
                curr.pop()
        
        generate([], 0)
    
        # print(ans)
        return ans