class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()
        q.append(beginWord)
        word_set = set(wordList)

        time = 0
        while q:
            time += 1
            len_q = len(q)
            for _ in range(len_q):
                word = q.popleft()
                if word == endWord:
                    return time
                for i in range(len(word)):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei in word_set:
                            q.append(nei)
                            word_set.remove(nei)
        return 0

