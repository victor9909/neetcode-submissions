class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        id_to_email = {}
        email_to_name = {}

        # Give every unique email an ID
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in email_to_id:
                    idx = len(email_to_id)
                    email_to_id[email] = idx
                    id_to_email[idx] = email

                email_to_name[email] = name

        n = len(email_to_id)
        adj_list = [[] for _ in range(n)]

        # Connect all emails in an account to the first email
        for account in accounts:
            first = email_to_id[account[1]]

            for email in account[2:]:
                curr = email_to_id[email]

                adj_list[first].append(curr)
                adj_list[curr].append(first)

        visited = set()
        result = []

        def dfs(node, group):
            if node in visited:
                return

            visited.add(node)
            group.append(node)

            for nei in adj_list[node]:
                dfs(nei, group)

        for node in range(n):
            if node in visited:
                continue

            group = []
            dfs(node, group)

            emails = [id_to_email[i] for i in group]
            emails.sort()

            name = email_to_name[emails[0]]
            result.append([name] + emails)

        return result