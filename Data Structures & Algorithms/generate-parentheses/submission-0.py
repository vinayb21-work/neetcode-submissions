class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def generate(n, i, left, right, curr):
            if right > left:
                return
            if i == 2 * n:
                if left == right:
                    self.ans.append(curr)
                return
            
            generate(n, i+1, left + 1, right, curr + "(")
            generate(n, i+1, left, right + 1, curr + ")")
        
        generate(n, 0, 0, 0, "")
    
        return self.ans