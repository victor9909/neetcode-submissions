import heapq

class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []

        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        users = set()

        if userId in self.follows:
            users = self.follows[userId].copy()

        users.add(userId)

        heap = []

        for user in users:
            if user in self.posts and self.posts[user]:
                idx = len(self.posts[user]) - 1
                time, tweet = self.posts[user][idx]

                heapq.heappush(
                    heap,
                    (-time, tweet, user, idx)
                )

        res = []

        while heap and len(res) < 10:
            _, tweet, user, idx = heapq.heappop(heap)
            res.append(tweet)

            if idx > 0:
                time, tweet = self.posts[user][idx - 1]

                heapq.heappush(
                    heap,
                    (-time, tweet, user, idx - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)