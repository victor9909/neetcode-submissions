class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        word_set = set(wordList)
        moves = 1

        while q:
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                if node == endWord:
                    return moves
                for i in range(len(node)):
                    for c in range(ord('a'), ord('z') + 1):
                        word = node[:i] + chr(c) + node[i + 1:]
                        if (word in visit or word not in word_set):
                            continue
                        q.append(word)
                        visit.add(word)
            moves += 1
        return 0
                
