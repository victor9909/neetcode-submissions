class FreqStack:

    def __init__(self):
        self.dict_cnt = defaultdict(int)
        self.max_cnt = 0
        self.dict_stacks = defaultdict(list)

    def push(self, val: int) -> None:
        cnt = self.dict_cnt[val] + 1
        self.dict_cnt[val] = cnt
        if cnt > self.max_cnt:
            self.max_cnt = cnt
        self.dict_stacks[cnt].append(val)

    def pop(self) -> int:
        res = self.dict_stacks[self.max_cnt].pop()
        self.dict_cnt[res] -= 1
        if not self.dict_stacks[self.max_cnt]:
            del self.dict_stacks[self.max_cnt]
            self.max_cnt -= 1
        if self.dict_cnt[res] == 0:
            del self.dict_cnt[res]
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()