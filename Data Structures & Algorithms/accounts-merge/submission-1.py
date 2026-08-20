class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_dict = {}
        idx = 0
        for a in accounts:
            for e in a[1:]:
                if e not in email_dict:
                    email_dict[e] = idx
                    idx += 1
        
        email_to_name = {}
        for a in accounts:
            for e in a[1:]:
                email_to_name[email_dict[e]] = (a[0], e)

        adj_list = {i:[] for i in range(idx)}
        for a in accounts:
            for e1 in a[1:]:
                for e2 in a[1:]:
                    if e1 != e2:
                        adj_list[email_dict[e1]].append(email_dict[e2])
        
        visit = set()
        res = []

        def dfs(node, group):

            if node in visit:
                return
            
            visit.add(node)
            for nei in adj_list[node]:
                dfs(nei, group)
            group.append(node)


        res = []
        for e in range(idx):
            group = []
            dfs(e, group)
            if group:
                res.append(group)
        
        final_r = []
        for g in res:
            curr_g = []
            name = email_to_name[g[0]][0]
            for e in g:
                curr_g.append(email_to_name[e][1])
            curr_g.sort()
            curr = [name] + curr_g
            final_r.append(curr)
        return final_r


        

            
                
                