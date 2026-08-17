class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
            
        deadends_set = set(deadends)
        q = deque(["0000"])
        visit = set()
        visit.add("0000")

        time = 0
        while q:
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                if node == target:
                    return time
                for i in range(4):
                    for j in [-1, 1]:
                        new_n = node[:i] + str((int(node[i]) + j) % 10) + node[i+1:]
                        if new_n not in visit and new_n not in deadends_set:
                            visit.add(new_n)
                            q.append(new_n)
            time += 1
        
        return -1
