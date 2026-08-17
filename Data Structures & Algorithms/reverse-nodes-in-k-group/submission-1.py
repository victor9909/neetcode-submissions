class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(l):
            prev = None
            curr = l

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev

        lists = []
        curr = head

        while curr:
            group_head = curr
            
            cnt = 0
            
            for _ in range(k - 1):
                if curr.next is None:
                    break
                cnt += 1
                curr = curr.next

            if cnt < k - 1:
                lists.append([group_head, curr])
                break

            next_group = curr.next
            curr.next = None

            new_h = reverse(group_head)
            lists.append([new_h, group_head])

            curr = next_group

        for i in range(len(lists) - 1):
            lists[i][1].next = lists[i + 1][0]

        return lists[0][0] if lists else head