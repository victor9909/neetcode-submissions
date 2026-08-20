class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # 0000
        
        # 1000 x 5 -> 5000
        # 0100 x 5 -> 5500
        # 0010 x 5 -> 5550
        # 0001 x 5 -> 5555

        q = deque()
        q.append("0000")
        visit = set()
        visit.add("0000")
        deadends_s = set(deadends)
        if "0000" in deadends_s:
            return -1
        moves = 0

        while q:
            len_q = len(q)
            for _ in range(len_q):
                num = q.popleft()
                if num == target:
                    return moves
                for i in range(4):
                    n = int(num[i])
                    for j in [-1, 1]:
                        digit = str((int(num[i]) + j + 10) % 10)
                        lock = num[:i] + digit + num[i + 1:]
                        if lock in deadends_s or lock in visit:
                            continue
                        visit.add(lock)
                        q.append(lock)
            moves += 1


        return -1


                    


