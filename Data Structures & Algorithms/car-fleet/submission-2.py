class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        stack = []
        n = len(position)
        positionSpeed = [(position[i], speed[i]) for i in range(n)]
        positionSpeed.sort(key=lambda x: -x[0])
        for p, s in positionSpeed:
            time = (target - p) / s
            # print(time)
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)

