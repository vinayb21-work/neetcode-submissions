class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        def check(counter1, counter2):
            for i in range(26):
                char = chr(97 + i)
                if counter1[char] > counter2[char]:
                    return False
            return True

        for i in range(m):
            counter1[s1[i]] += 1
            counter2[s2[i]] += 1
        
        if check(counter1, counter2):
            return True
        
        for i in range(m, n):
            counter2[s2[i-m]] -= 1
            counter2[s2[i]] += 1
            if check(counter1, counter2):
                return True
        
        return False