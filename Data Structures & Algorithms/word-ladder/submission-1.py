class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_set = set(wordList)
        q = deque([beginWord])

        time = 0
        while q:
            len_q = len(q)
            time += 1
            for i in range(len_q):
                word = q.popleft()
                if word == endWord:
                    return time
                for i in range(len(word)):
                    for c in range(ord('a'), ord('z') + 1):
                        new_w = word[:i] + chr(c) + word[i + 1:]
                        if new_w in word_set:
                            q.append(new_w)
                            word_set.remove(new_w)
        
        return 0